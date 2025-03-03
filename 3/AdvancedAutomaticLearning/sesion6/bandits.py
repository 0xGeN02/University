import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, true_reward):
        self.true_reward = true_reward  # True reward probability
        self.estimated_reward = 0  # Estimated reward (starts at 0)
        self.N = 0  # Number of times pulled

    def pull(self):
        """Simulate pulling the bandit arm (Bernoulli trial)"""
        return np.random.binomial(1, self.true_reward)

    def update(self, reward):
        """Update the estimated reward"""
        self.N += 1
        self.estimated_reward = (self.estimated_reward * (self.N - 1) + reward) / self.N


def create_bandits(num_bandits):
    """Create bandits with random true rewards and print their probabilities"""
    true_rewards = np.random.rand(num_bandits)
    bandits = [Bandit(p) for p in true_rewards]

    print("\nBandit True Probabilities:")
    for i, bandit in enumerate(bandits):
        print(f"Bandit {i + 1}: {bandit.true_reward:.2f}")

    return bandits


def naive_algorithm(bandits, total_trials, explore_trials=10):
    """Naive algorithm: explore first, then exploit"""
    rewards = np.zeros(total_trials)
    for i in range(explore_trials):
        reward = bandits[i].pull()
        bandits[i].update(reward)
        rewards[i] = reward

    for i in range(explore_trials, total_trials):
        best_bandit = np.argmax([bandit.estimated_reward for bandit in bandits])
        reward = bandits[best_bandit].pull()
        bandits[best_bandit].update(reward)
        rewards[i] = reward

    return np.cumsum(rewards)


def epsilon_greedy(bandits, total_trials, epsilon=0.1):
    """ε-Greedy algorithm: explore with probability ε, exploit with probability 1-ε"""
    rewards = np.zeros(total_trials)
    for i in range(total_trials):
        if np.random.rand() < epsilon:
            bandit = np.random.choice(bandits)
        else:
            bandit = bandits[np.argmax([b.estimated_reward for b in bandits])]

        reward = bandit.pull()
        bandit.update(reward)
        rewards[i] = reward

    return np.cumsum(rewards)


# Parameters
num_bandits = 100
total_trials = 10000

# Create bandits and show probabilities
bandits = create_bandits(num_bandits)

# Run both algorithms
naive_rewards = naive_algorithm(bandits, total_trials, explore_trials=10)
epsilon_rewards = epsilon_greedy(bandits, total_trials, epsilon=0.1)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(naive_rewards, label="Naive (Explore First)")
plt.plot(epsilon_rewards, label="ε-Greedy (ε=0.1)")
plt.xlabel("Trials")
plt.ylabel("Cumulative Reward")
plt.title("Multi-Armed Bandit: Naive vs ε-Greedy")
plt.legend()
plt.show()
plt.savefig(r"C:\Users\manue\University\3\AdvancedAutomaticLearning\sesion6\bandits_plot.png")
