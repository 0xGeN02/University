# USAGE
# python train.py

# import the necessary packages
import os
from pathlib import Path

import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import OxfordIIITPet
from tqdm import tqdm

from pyimagesearch import config, data_utils, model_utils, network

def main():
    # create parent folder to store all the results
    parent_folder = "output"
    if not os.path.exists(parent_folder):
        os.makedirs(parent_folder)


    print("[INFO] Fetching the Oxford IIIT Pet Dataset from cache or downloading it")
    # load the dataset
    dataset = OxfordIIITPet(
        root=config.DATA_DIR, target_types="segmentation", download=True
    )

    # define the paths to the images and segmentation maps directories
    images_dir = "./data/oxford-iiit-pet/images"
    mask_dir = "./data/oxford-iiit-pet/annotations/trimaps"

    print("[INFO] Preparing the dataset for training")
    # initialize the OxfordPetDataset class
    dataset = data_utils.OxfordPetDataset(images_dir=images_dir, mask_dir=mask_dir)

    # split into train / validation partitions
    n_val = int(len(dataset) * config.VAL_PERCENT)
    n_train = len(dataset) - n_val
    train_set, val_set = random_split(
        dataset, [n_train, n_val], generator=torch.Generator().manual_seed(0)
    )

    # create data loaders for training and validation
    train_loader = DataLoader(train_set, batch_size=config.BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(
        val_set, batch_size=config.BATCH_SIZE, shuffle=False, drop_last=True
    )

    # call the UNet class from the network.py file and initialize the model
    model = network.CustomUNet(input_channels=3, num_classes=3)
    model.to(device=config.DEVICE)

    # set up the optimizer, the categorical loss, the learning rate scheduler
    optimizer = optim.RMSprop(
        model.parameters(),
        lr=config.LEARNING_RATE,
        weight_decay=config.WEIGHT_DECAY,
        momentum=config.MOMENTUM,
        foreach=True,
    )
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, "max", patience=5
    )  # goal: maximize Dice score
    criterion = nn.CrossEntropyLoss()

    # initialize lists for storing loss and validation Dice scores over epochs
    epoch_losses = []
    val_scores = []
    train_scores = []
    val_losses = []

    print("[INFO] Starting training")
    # begin training
    for epoch in range(1, config.EPOCHS + 1):
        # set the model to training mode
        model.train()
        # initialize the epoch loss and epoch Dice score variables to store the loss and Dice score for each epoch
        epoch_loss = 0
        epoch_dice_score = 0
        # create a progress bar for training and wrap it with tqdm to display progress during training
        with tqdm(total=n_train, desc=f"Epoch {epoch}/{config.EPOCHS}", unit="img") as pbar:
            # iterate over the training set
            for batch in train_loader:
                # extract the image and mask batch, and move the batch to the device
                images, true_masks = batch["image"], batch["mask"]

                # move images and masks to correct device and type
                images = images.to(
                    device=config.DEVICE,
                    dtype=torch.float32,
                    memory_format=torch.channels_last,
                )
                true_masks = true_masks.to(device=config.DEVICE, dtype=torch.long)

                # predict the mask using the model
                masks_pred = model(images)

                # compute the cross-entropy loss and the Dice loss for the predicted masks vs. the true masks
                loss = criterion(masks_pred, true_masks)
                loss += model_utils.dice_loss(true_masks, masks_pred)

                # zero the gradients
                optimizer.zero_grad(set_to_none=True)
                # backpropagate the loss
                loss.backward()
                # clip the gradients to prevent exploding gradients
                torch.nn.utils.clip_grad_norm_(model.parameters(), config.GRADIENT_CLIPPING)
                # update the weights
                optimizer.step()

                # update the progress bar
                pbar.update(images.shape[0])

                # update the epoch loss
                epoch_loss += loss.item()
                # update the progress bar with the loss for the current batch
                pbar.set_postfix(**{"loss (batch)": loss.item()})

                # compute Dice score for training set for this batch and add it to the epoch Dice score
                dice_score_batch = model_utils.multi_class_dice_coeff(
                    true_masks, masks_pred
                )
                epoch_dice_score += (
                    dice_score_batch.item()
                )  # Sum up the Dice score for each batch

        # compute average loss and Dice score for this epoch
        avg_loss = epoch_loss / len(train_loader)
        avg_dice_score = epoch_dice_score / len(train_loader)
        # append the average loss and Dice score to the respective lists
        epoch_losses.append(avg_loss)
        train_scores.append(avg_dice_score)

        # print the average loss and Dice score for this epoch
        print(
            f"[INFO] Epoch {epoch} finished! Loss: {avg_loss}, Train Dice Score: {avg_dice_score}"
        )

        # evaluation at the end of the epoch on the validation set
        val_score, val_loss = model_utils.evaluate(
            model, val_loader, config.DEVICE, criterion=criterion
        )
        # update the learning rate scheduler based on the validation Dice score
        scheduler.step(val_score)
        # print the validation loss and Dice score for this epoch
        print(f"[INFO] Validation Loss: {val_loss}, Validation Dice score: {val_score}")
        # append the validation loss and Dice score to the respective lists
        val_losses.append(val_loss)
        val_scores.append(val_score)
        # visualize one random test image and its corresponding predicted and ground truth masks per epoch
        model_utils.test_model(
            model, config.DEVICE, val_loader, epoch, parent_folder=parent_folder
        )

        # save the model checkpoint after each epoch
        Path(parent_folder, config.MODEL_CHECKPOINT_DIR).mkdir(parents=True, exist_ok=True)
        state_dict = model.state_dict()
        state_dict["mask_values"] = dataset.mask_values

        # construct the path for saving the checkpoint
        checkpoint_path = os.path.join(
            parent_folder, config.MODEL_CHECKPOINT_DIR, f"checkpoint_epoch{epoch}.pth"
        )
        torch.save(state_dict, checkpoint_path)
        print(f"[INFO] Checkpoint {epoch} saved at: {checkpoint_path}")

    print(
        "[INFO] Training is completed, let's now run the inference with trained UNET on the test set"
    )
    model_utils.test_model_post_training(
        model, config.DEVICE, val_loader, epoch, sample_size=50, parent_folder=parent_folder
    )


if __name__ == "__main__":
    main()
