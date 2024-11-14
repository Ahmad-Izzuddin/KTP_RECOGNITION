import cv2

class ImageProcessor:
    def preprocess(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blurred = cv2.GaussianBlur(binary, (3, 3), 0)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        morphed = cv2.dilate(blurred, kernel, iterations=1)
        return cv2.convertScaleAbs(morphed, alpha=1.5, beta=30)