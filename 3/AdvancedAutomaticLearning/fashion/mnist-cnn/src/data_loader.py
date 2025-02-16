"""
Load data from a CSV file and return the images and labels as numpy arrays.
"""
import os
import sys
import pandas as pd

# Add the parent directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import FASHION_CSV

def load_data(csv_path):
    """
    Load data from a CSV file and return the images and labels as numpy arrays.
    """
    data = pd.read_csv(csv_path)
    data_labels = data['label'].values
    data_images = data.drop(columns=['label']).values
    data_images = data_images.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    return data_images, data_labels

if __name__ == "__main__":
    images, labels = load_data(FASHION_CSV)
    print(f"Loaded {len(images)} images with shape {images[0].shape}")
