import pytesseract

class OcrProcessor:
    def __init__(self):
        #! for windows
        pytesseract.pytesseract.tesseract_cmd = r'D:/Application/Developer Tool/TESSERACT-OCR/tesseract.exe'

        #! for linux
        # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    def extract_text(self, image):
        return pytesseract.image_to_string(image, lang='ocraext')