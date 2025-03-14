# import the necessary packages
import torch
import torch.nn as nn
import torch.nn.functional as F


class DualConv(nn.Module):
    def __init__(self, input_ch, output_ch):
        super(DualConv, self).__init__()
        self.conv_block = nn.Sequential(
            nn.Conv2d(input_ch, output_ch, 3, padding=1, bias=False),
            nn.BatchNorm2d(output_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(output_ch, output_ch, 3, padding=1, bias=False),
            nn.BatchNorm2d(output_ch),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.conv_block(x)


class Contract(nn.Module):
    def __init__(self, input_ch, output_ch):
        super(Contract, self).__init__()
        self.down_conv = nn.Sequential(nn.MaxPool2d(2), DualConv(input_ch, output_ch))

    def forward(self, x):
        return self.down_conv(x)


class Expand(nn.Module):
    def __init__(self, input_ch, output_ch):
        super(Expand, self).__init__()
        self.up = nn.ConvTranspose2d(input_ch, input_ch // 2, kernel_size=2, stride=2)
        self.conv = DualConv(input_ch, output_ch)

    def forward(self, x1, x2):
        x1 = self.up(x1)
        diff_y = x2.size()[2] - x1.size()[2]
        diff_x = x2.size()[3] - x1.size()[3]
        x1 = F.pad(
            x1, [diff_x // 2, diff_x - diff_x // 2, diff_y // 2, diff_y - diff_y // 2]
        )
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)


class FinalConv(nn.Module):
    def __init__(self, input_ch, output_ch):
        super(FinalConv, self).__init__()
        self.conv = nn.Conv2d(input_ch, output_ch, kernel_size=1)

    def forward(self, x):
        return self.conv(x)


class CustomUNet(nn.Module):
    def __init__(self, input_channels, num_classes):
        super(CustomUNet, self).__init__()
        self.initial = DualConv(input_channels, 64)
        self.down1 = Contract(64, 128)
        self.down2 = Contract(128, 256)
        self.down3 = Contract(256, 512)
        self.down4 = Contract(512, 1024)
        self.up1 = Expand(1024, 512)
        self.up2 = Expand(512, 256)
        self.up3 = Expand(256, 128)
        self.up4 = Expand(128, 64)
        self.final = FinalConv(64, num_classes)

    def forward(self, x):
        x1 = self.initial(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x = self.up1(x5, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        logits = self.final(x)
        return logits
