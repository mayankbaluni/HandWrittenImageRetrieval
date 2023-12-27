from skimage import io, color, transform
import os

def preprocess_images(image_folder):
    processed_images = []
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg'):  # assuming images are in JPG format
            image = io.imread(os.path.join(image_folder, filename))
            image_bw = color.rgb2gray(image)  # Convert to grayscale
            image_resized = transform.resize(image_bw, (128, 128))  # Resize to uniform size
            processed_images.append(image_resized)
    return processed_images

# Example usage
image_folder = 'path_to_image_folder'
images = preprocess_images(image_folder)
