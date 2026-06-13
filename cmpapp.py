from scipy.fftpack import dct, idct
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import tkinter as tk
from tkinter import filedialog

# DCT and IDCT functions
# frequency transform
def dct2(block):                                #Converts image from spatial domain to frequency domain.
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

#deconstruction
def idct2(block):                                #Converts frequency data back to image
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

#COMPRESSION FUNCTION -     Performs image compression using DCT
def compress_color_image(image):                   
    # Reduce resolution (half size) for faster processing
    image = transform.resize(image,(image.shape[0]//2, image.shape[1]//2), anti_aliasing=True)

    # If grayscale, just one channel
    if image.ndim == 2:
        #Convert to frequency domain
        dct_image = dct2(image)
        #Keep only important values
        threshold = 0.001 * np.max(np.abs(dct_image))
        dct_compressed = dct_image * (np.abs(dct_image) > threshold)
        #Reconstruct image
        reconstructed = idct2(dct_compressed)
        return image, reconstructed

    # If color, process each channel separately
    channels = []
    for c in range(3):
        #Apply DCT to each color
        dct_image = dct2(image[:,:,c])
        #remove all small values
        threshold = 0.001 * np.max(np.abs(dct_image))
        dct_compressed = dct_image * (np.abs(dct_image) > threshold)
        #rebuild channel
        reconstructed_channel = idct2(dct_compressed)
        channels.append(reconstructed_channel)
    #Combine R,G,B Channels
    reconstructed = np.stack(channels, axis=2)
    return image, reconstructed

def add_picture(event):       #load image button function
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff")]
    )
    if not file_path:
        return

    image = io.imread(file_path)
    original, reconstructed = compress_color_image(image)          

    # Show results: only Original and Compressed
    fig2, ax2 = plt.subplots(1,2, figsize=(12,5))
    ax2[0].imshow(original)
    ax2[0].set_title("Original")
    ax2[0].axis('off')

    ax2[1].imshow(np.clip(reconstructed, 0, 1))
    ax2[1].set_title("Compressed (DCT)")
    ax2[1].axis('off')

    plt.show()

# Initial empty figure with button only
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.axis('off')

ax_button = plt.axes([0.7, 0.05, 0.2, 0.075])
button = Button(ax_button, 'Add Picture')
button.on_clicked(add_picture)

plt.show()
