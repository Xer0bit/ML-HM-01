import numpy as np
from PIL import Image
from scipy import ndimage

def ImagePP(img):
    custom_image = Image.open(img)
    custom_image = custom_image.convert('L')  # Convert to grayscale
    custom_image = custom_image.resize((28, 28))  # Resize to match MNIST input size
    custom_image = np.array(custom_image) / 255.0  # Normalize pixel values

    #invert the image
    custom_image = 1 - custom_image

    #sharpe the image
    custom_image = ndimage.gaussian_filter(custom_image, sigma=0.1)

    #Image enhancement
    custom_image[custom_image < 0.1] = 0


    # Reshape the custom image to match the expected input shape
    custom_image = custom_image.reshape(1, 784)  # Reshape to (1, 784)

    return custom_image

# custom_image = ImagePP("/home/xer0bit/Desktop/SEN-321/Homework-1/code/test.png")
# print(custom_image.shape)
