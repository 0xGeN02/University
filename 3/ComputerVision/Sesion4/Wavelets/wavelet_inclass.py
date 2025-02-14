"""
Simplified Two-Dimensional Wavelet Transform Example
Requirements: numpy, matplotlib, pywavelets
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt

def create_test_image(size=256):
    """Create a test image with clear patterns"""
    img = np.zeros((size, size))
    
    # Add a central square
    img[size//4:3*size//4, size//4:3*size//4] = 1
    
    # Add some diagonal lines
    for i in range(size):
        img[i, i] = 1
        if i < size-1:
            img[i, size-i-1] = 1
    
    # Add horizontal and vertical lines
    img[size//2, :] = 1
    img[:, size//2] = 1
    
    return img

def normalize_for_display(data):
    """Normalize data for better visualization"""
    data_min = np.min(data)
    data_max = np.max(data)
    if data_max == data_min:
        return np.zeros_like(data)
    return (data - data_min) / (data_max - data_min)

def compare_wavelets():
    """Compare different wavelets on the same image"""
    # Create test image
    image = create_test_image(256)
    
    # List of wavelets to compare
    wavelets = ['haar', 'db4', 'sym4']
    
    # Create figure for original image
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray')
    plt.title('Original Test Image')
    plt.axis('off')
    plt.show()
    
    # Process each wavelet
    for wavelet in wavelets:
        # Perform 2D DWT
        coeffs = pywt.dwt2(image, wavelet, mode='periodic')
        LL, (LH, HL, HH) = coeffs
        
        # Create figure
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        fig.suptitle(f'Wavelet Transform using {wavelet}', fontsize=16)
        
        # Plot approximation
        axes[0, 0].imshow(normalize_for_display(LL), cmap='gray')
        axes[0, 0].set_title('LL - Approximation')
        axes[0, 0].axis('off')
        
        # Plot horizontal details
        axes[0, 1].imshow(normalize_for_display(LH), cmap='gray')
        axes[0, 1].set_title('LH - Horizontal Details')
        axes[0, 1].axis('off')
        
        # Plot vertical details
        axes[1, 0].imshow(normalize_for_display(HL), cmap='gray')
        axes[1, 0].set_title('HL - Vertical Details')
        axes[1, 0].axis('off')
        
        # Plot diagonal details
        axes[1, 1].imshow(normalize_for_display(HH), cmap='gray')
        axes[1, 1].set_title('HH - Diagonal Details')
        axes[1, 1].axis('off')
        
        plt.tight_layout()
        plt.show()
        
        # Reconstruct and show the difference
        reconstructed = pywt.idwt2(coeffs, wavelet)
        
        # Show original vs reconstructed
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
        
        ax1.imshow(image, cmap='gray')
        ax1.set_title('Original Image')
        ax1.axis('off')
        
        ax2.imshow(normalize_for_display(reconstructed), cmap='gray')
        ax2.set_title(f'Reconstructed Image ({wavelet})')
        ax2.axis('off')
        
        plt.show()

if __name__ == "__main__":
    compare_wavelets()