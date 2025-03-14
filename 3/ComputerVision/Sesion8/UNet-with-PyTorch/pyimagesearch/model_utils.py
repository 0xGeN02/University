import matplotlib
import torch
import torch.nn.functional as F
from tqdm import tqdm

matplotlib.use("Agg")
import os
import random

import matplotlib.pyplot as plt
import numpy as np


def multi_class_dice_coeff(true, logits, eps=1e-7):
    """Computes the Sørensen-Dice coefficient for multi-class.

    Args:
        true: a tensor of shape [B, 1, H, W].
        logits: a tensor of shape [B, C, H, W]. Corresponds to
            the raw output or logits of the model.
        eps: added to the denominator for numerical stability.

    Returns:
        dice_coeff: the Sørensen-Dice coefficient.
    """
    num_classes = logits.shape[1]
    true_1_hot = torch.eye(num_classes)[true.squeeze(1)]
    true_1_hot = true_1_hot.permute(0, 3, 1, 2).float()
    probas = F.softmax(logits, dim=1)
    true_1_hot = true_1_hot.type(logits.type())
    dims = (0,) + tuple(range(2, true.ndimension()))
    intersection = torch.sum(probas * true_1_hot, dims)
    cardinality = torch.sum(probas + true_1_hot, dims)
    dice_coeff = (2.0 * intersection / (cardinality + eps)).mean()
    return dice_coeff


def dice_loss(true, logits, eps=1e-7):
    """Computes the Sørensen-Dice loss, which is 1 minus the Dice coefficient.

    Args:
        true: a tensor of shape [B, 1, H, W].
        logits: a tensor of shape [B, C, H, W]. Corresponds to
            the raw output or logits of the model.
        eps: added to the denominator for numerical stability.

    Returns:
        dice_loss: the Sørensen-Dice loss.
    """
    return 1 - multi_class_dice_coeff(true, logits, eps)


@torch.inference_mode()
def evaluate(net, dataloader, device, criterion):
    net.eval()
    num_val_batches = len(dataloader)
    dice_score = 0
    cross_entropy_loss = 0
    dice_loss_val = 0  # initialize Dice loss for validation set

    # iterate over the validation set
    for batch in tqdm(
        dataloader,
        total=num_val_batches,
        desc="Validation round",
        unit="batch",
        leave=False,
    ):
        image, mask_true = batch["image"], batch["mask"]

        # move images and labels to correct device and type
        image = image.to(
            device=device, dtype=torch.float32, memory_format=torch.channels_last
        )
        mask_true = mask_true.to(device=device, dtype=torch.long)

        # predict the mask
        mask_pred = net(image)

        # compute the Cross-Entropy loss
        cross_entropy_loss += criterion(mask_pred, mask_true).item()

        # Compute Dice loss for validation set
        dice = dice_loss(mask_true, mask_pred)
        dice_loss_val += dice.item()

        # compute the Dice score
        dice_score += multi_class_dice_coeff(mask_true, mask_pred)

    # switch the network back to training mode
    net.train()

    # compute the average Dice score and loss
    avg_dice_score = dice_score / max(num_val_batches, 1)
    avg_cross_entropy_loss = cross_entropy_loss / max(num_val_batches, 1)
    avg_dice_loss_val = dice_loss_val / max(num_val_batches, 1)

    # Compute combined loss
    avg_combined_loss = avg_cross_entropy_loss + avg_dice_loss_val

    # return the average Dice score and loss
    return avg_dice_score, avg_combined_loss


def test_model(model, device, test_loader, epoch, parent_folder="output"):
    """
    Save one random test image and its corresponding predicted and ground truth masks per epoch.

    Args:
        model (torch.nn.Module): The trained model.
        device (torch.device): The device (cpu or cuda).
        test_loader (torch.utils.data.DataLoader): DataLoader for the test dataset.
        epoch (int): The current epoch.
    """
    # set the model to evaluation mode
    model.eval()

    # create a folder to save the images
    output_folder = os.path.join(parent_folder, "infer_train_images")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # no need to track gradients
    with torch.no_grad():
        # randomly select a batch from the test set
        random_batch = random.choice([batch for batch in test_loader])
        # extract the image and mask batch, and move the batch to the device
        images, true_masks = random_batch["image"], random_batch["mask"]
        images = images.to(device=device, dtype=torch.float32)

        # predict masks for the image batch
        predicted_masks = model(images)

        # take the argmax to get the most likely class
        predicted_masks = torch.argmax(predicted_masks, dim=1)

        # randomly select an input image, predicted mask, and true mask from the batch
        random_index = random.randint(0, len(images) - 1)
        img, pred_mask, true_mask = (
            images[random_index],
            predicted_masks[random_index],
            true_masks[random_index],
        )

        # plot the image and the ground truth and predicted masks
        fig, ax = plt.subplots(1, 3)

        ax[0].imshow(img.permute(1, 2, 0).cpu().numpy())
        ax[0].set_title("Test Image")
        ax[0].axis("off")

        ax[1].imshow(pred_mask.cpu().numpy())
        ax[1].set_title("Predicted Mask")
        ax[1].axis("off")

        ax[2].imshow(true_mask.cpu().numpy())
        ax[2].set_title("Ground Truth Mask")
        ax[2].axis("off")

        # save the figure with some padding at the bottom
        plt.savefig(
            os.path.join(output_folder, f"epoch_{epoch}_image.png"),
            bbox_inches="tight",
            pad_inches=0.1,
        )


def test_model_post_training(
    model, device, test_loader, sample_size=50, parent_folder="output"
):
    """
    visualize 50 random test images and their corresponding predicted and ground truth masks per epoch.

    Args:
        model (torch.nn.Module): The trained model.
        device (torch.device): The device (cpu or cuda).
        test_loader (torch.utils.data.DataLoader): DataLoader for the test dataset.
        epoch (int): The current epoch.
    """
    # set the model to evaluation mode
    model.eval()

    # create a folder to save the images
    output_folder = os.path.join(parent_folder, "infer_test_images_post_training")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # initialize lists to store the images, predicted masks, and true masks
    all_images = []
    all_pred_masks = []
    all_true_masks = []

    with torch.no_grad():  # no need to track gradients
        for batch in test_loader:
            # extract the image and mask batch, and move the batch to the device
            images, true_masks = batch["image"], batch["mask"]
            images = images.to(device=device, dtype=torch.float32)

            # predict masks for the image batch using the trained model
            predicted_masks = model(images)

            # take the argmax to get the most likely class
            predicted_masks = torch.argmax(predicted_masks, dim=1)

            # append the images, predicted masks, and true masks to the lists
            all_images.extend(images)
            all_pred_masks.extend(predicted_masks)
            all_true_masks.extend(true_masks)

        # randomly select sample_size images from the test set
        random_indices = np.random.choice(
            len(all_images), size=sample_size, replace=False
        )

        for i in random_indices:
            # randomly select an input image, predicted mask, and true mask from the batch
            img, pred_mask, true_mask = (
                all_images[i],
                all_pred_masks[i],
                all_true_masks[i],
            )

            # plot the image and the ground truth and predicted masks
            fig, ax = plt.subplots(1, 3)

            ax[0].imshow(img.permute(1, 2, 0).cpu().numpy())
            ax[0].set_title("Test Image")
            ax[0].axis("off")

            ax[1].imshow(pred_mask.cpu().numpy())
            ax[1].set_title("Predicted Mask")
            ax[1].axis("off")

            ax[2].imshow(true_mask.cpu().numpy())
            ax[2].set_title("Ground Truth Mask")
            ax[2].axis("off")

            # save the figure with some padding at the bottom
            plt.savefig(
                os.path.join(output_folder, f"validation_image_{i}.png"),
                bbox_inches="tight",
                pad_inches=0.1,
            )
            plt.close(fig)  # close the plot to free up memory
