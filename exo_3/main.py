import numpy as np
import random

# Global variable for Gaussian noise dithering
WITH_GAUSSIAN_NOISE = False

def group_and_split_highest_chanel_range(pixels, nb_colors_stop) -> list[np.ndarray]:
    
    if nb_colors_stop == 1:
        return [pixels]

    # Split the pixel space along the largest color range
    ranges = np.ptp(pixels, axis=0)
    split_index = np.argmax(ranges)
    pixels_sorted = pixels[:, split_index].argsort()
    split_index = len(pixels_sorted) // 2
    pixels_left = pixels[pixels_sorted[:split_index]]
    pixels_right = pixels[pixels_sorted[split_index:]]

    return group_and_split_highest_chanel_range(pixels_left, nb_colors_stop // 2) + group_and_split_highest_chanel_range(pixels_right, nb_colors_stop - nb_colors_stop // 2)

def quantize_median_cut(image, n_colors):
    # Reshape the image into a 2D array of pixels
    pixels = np.reshape(image, (-1, 3))

    pixel_groups = group_and_split_highest_chanel_range(pixels, n_colors)

    # for each group, compute the mean of each color channel, which will be the color of the palette
    palette = np.array([np.mean(group, axis=0) for group in pixel_groups])

    # Replace each pixel with the closest palette color
    distances = np.sqrt(np.sum((pixels[:, np.newaxis] - palette) ** 2, axis=2))

    # Apply Gaussian noise dithering, if enabled
    if WITH_GAUSSIAN_NOISE:
        noise = np.random.normal(0, 10.5, size=distances.shape)
        distances += noise

    labels = np.argmin(distances, axis=1)
    quantized = palette[labels]

    # Reshape the quantized image back into its original shape
    quantized = np.reshape(quantized, image.shape)

    return quantized

# main
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import os

    # Load the image
    image = mpimg.imread(os.path.join(os.path.dirname(__file__), "img/Angel-of-Sanctions-Amonkhet-MtG-Art.jpg"))

    # Quantize the image
    quantized = quantize_median_cut(image.astype(float), 6)  # Convert image to float type

    # Normalize the quantized image to the range [0, 1]
    quantized_normalized = quantized / 255

    # Show the image
    plt.imshow(quantized_normalized)
    plt.show()

    # Save the image
    mpimg.imsave(os.path.join(os.path.dirname(__file__), "img/quantized.png"), quantized_normalized)
