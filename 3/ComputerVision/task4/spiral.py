"""
Implementación de Discrete Flow Matching para una distribución en espiral discreta
Referencia principal: "Discrete Flow Matching" (Gat et al., NeurIPS 2024)
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

# 1. Generación de datos: espiral discreta
class SpiralDataset(Dataset):
    def __init__(self, num_points=10000, num_bins=32, noise=0.1):
        self.num_bins = num_bins
        a, b = 0.5, 0.2
        thetas = np.linspace(0, 4 * np.pi, num_points)
        rs = a + b * thetas
        xs = rs * np.cos(thetas) + noise * np.random.randn(num_points)
        ys = rs * np.sin(thetas) + noise * np.random.randn(num_points)
        xs = (xs - xs.min()) / (xs.max() - xs.min())
        ys = (ys - ys.min()) / (ys.max() - ys.min())
        bins = np.linspace(0, 1, num_bins + 1)
        xi = np.digitize(xs, bins) - 1
        yi = np.digitize(ys, bins) - 1
        self.data = xi * num_bins + yi

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx], dtype=torch.long)

# 2. Modelo: CTMC Flow Matching
class CTMCFlowMatching(nn.Module):
    def __init__(self, num_bins, hidden_dim=128):
        super().__init__()
        self.num_bins = num_bins
        self.embed = nn.Embedding(num_bins * num_bins, hidden_dim)
        self.time_embed = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.net = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_bins * num_bins)
        )

    def forward(self, x, t):
        h = self.embed(x)
        te = self.time_embed(t.view(-1, 1).to(h.dtype))
        h = h + te
        rates = self.net(h)
        return rates.view(-1, self.num_bins, self.num_bins)

# 3. Pérdida Flow Matching discreta corregida
def flow_matching_loss(model, x, t, num_bins):
    pred = model(x, t)
    batch_size = x.size(0)
    # true rates: one-hot at current state * (1 - t)
    # flat one-hot: (batch, num_bins^2)
    true_flat = F.one_hot(x, num_bins * num_bins).to(torch.float32)
    # scale by (1 - t)
    scale = (1 - t).view(-1, 1)
    true_flat = true_flat * scale
    # reshape to (batch, num_bins, num_bins)
    true_rates = true_flat.view(batch_size, num_bins, num_bins).to(pred.device)
    # MSE
    return ((pred - true_rates) ** 2).mean()

# 4. Entrenamiento
def train(model, loader, num_bins, epochs=10):
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    for epoch in range(epochs):
        total_loss = 0.0
        for x in loader:
            x = x.view(-1)
            batch_size = x.size(0)
            t = torch.rand(batch_size)
            loss = flow_matching_loss(model, x, t, num_bins)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * batch_size
        print(f"Epoch {epoch}: Loss = {total_loss / len(loader.dataset):.6f}")

# 5. Muestreo por CTMC
@torch.no_grad()
def sample(model, num_bins, num_samples=1000, steps=10):
    x = torch.randint(0, num_bins * num_bins, (num_samples,))
    times = torch.linspace(1, 0, steps=steps)
    for t in times:
        rates = model(x, t.repeat(num_samples))
        probs = torch.softmax(rates.view(num_samples, -1), dim=1)
        x = torch.multinomial(probs, num_samples=1).view(-1)
    return x

if __name__ == "__main__":
    num_bins = 32
    dataset = SpiralDataset(num_points=10000, num_bins=num_bins)
    loader = DataLoader(dataset, batch_size=128, shuffle=True)

    model = CTMCFlowMatching(num_bins=num_bins)
    train(model, loader, num_bins=num_bins, epochs=30)

    samples = sample(model, num_bins=num_bins, num_samples=2000)
    xi = (samples // num_bins).numpy() / num_bins
    yi = (samples % num_bins).numpy() / num_bins
    np.savetxt("samples_spiral.csv", np.vstack([xi, yi]).T, delimiter=",")
    print("Muestras guardadas en samples_spiral.csv")
