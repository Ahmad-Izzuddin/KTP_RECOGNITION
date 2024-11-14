import cv2

from static.StaticPath import StaticPath

class OutputHandler:
    def __init__(self):
        self.preprocessing_output = StaticPath.PREPROCESSING_OUTPUT
        self.text_output = StaticPath.TEXT_OUTPUT

    def save_image(self, image, filename):
        cv2.imwrite(filename, image)

    def save_text(self, text, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)