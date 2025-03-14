# import the necessary packages
import os

# define the dataset directory by constructing the relative path to the data folder in the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
# define the path to the checkpoint
MODEL_CHECKPOINT_DIR = "model_weights"
# define the validation percentage
VAL_PERCENT = 0.1
# batch size for training
BATCH_SIZE = 128
# learning rate for the optimizer
LEARNING_RATE = 1e-5
# momentum for the optimizer
MOMENTUM = 0.999
# gradient clipping value (for stability while training)
GRADIENT_CLIPPING = 1.0
# weight decay (L2 regularization) for the optimizer
WEIGHT_DECAY = 1e-8
# number of epochs for training
EPOCHS = 1
# set device to 'cuda' if CUDA is available, 'cpu' otherwise for model training and testing
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
