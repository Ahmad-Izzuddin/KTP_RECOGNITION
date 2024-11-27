import cv2
import yaml
import numpy as np
from PIL import Image, ImageEnhance

class ImageProcessor:
    def __init__(self, config_file='config.yaml'):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def preprocess(self, image):
        brightness_factor = self.config['preprocessing']['brightness_factor']
        contrast_factor = self.config['preprocessing']['contrast_factor']
        dilation_kernel_size = self.config['preprocessing']['dilation_kernel_size']
        gaussian_blur_kernel_size = self.config['preprocessing']['gaussian_blur']['kernel_size']
        gaussian_blur_sigma_x = self.config['preprocessing']['gaussian_blur']['sigma_x']
        scale_alpha = self.config['preprocessing']['scale_alpha']
        scale_beta = self.config['preprocessing']['scale_beta']
        lower_black = np.array(self.config['preprocessing']['black_range']['lower'])
        upper_black = np.array(self.config['preprocessing']['black_range']['upper'])

        pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        mask = cv2.inRange(image, lower_black, upper_black)
        preprocessed_image = image.copy()
        preprocessed_image[mask == 0] = [255, 255, 255]

        pil_img = Image.fromarray(cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2RGB))

        brightness_enhancer = ImageEnhance.Brightness(pil_img)
        brighter_image = brightness_enhancer.enhance(brightness_factor)

        grayscale_image = brighter_image.convert('L')

        contrast_enhancer = ImageEnhance.Contrast(grayscale_image)
        contrasted_image = contrast_enhancer.enhance(contrast_factor)

        processed_image = np.array(contrasted_image)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (dilation_kernel_size, dilation_kernel_size))
        opened_image = cv2.morphologyEx(processed_image, cv2.MORPH_OPEN, kernel)

        scaled_image = cv2.convertScaleAbs(opened_image, alpha=scale_alpha, beta=scale_beta)

        if gaussian_blur_kernel_size % 2 == 0:  # Ensure odd kernel size
            gaussian_blur_kernel_size += 1
        blurred_image = cv2.GaussianBlur(scaled_image, (gaussian_blur_kernel_size, gaussian_blur_kernel_size), sigmaX=gaussian_blur_sigma_x)

        kernel_noise = np.ones((1, 1), np.uint8)
        cleaned = cv2.morphologyEx(blurred_image, cv2.MORPH_CLOSE, kernel_noise)

        return cv2.cvtColor(cleaned, cv2.COLOR_GRAY2BGR)