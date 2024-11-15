import pytesseract
import platform

from static.StaticPath import StaticPath
from static.StaticConstant import StaticConstant

class OcrProcessor:
    def __init__(self):
        if platform.system() == StaticConstant.DEFAULT_PLATFORM:
            pytesseract.pytesseract.tesseract_cmd = StaticPath.PYTESSERACT_WINDOWS
        else:
            pytesseract.pytesseract.tesseract_cmd = StaticPath.PYTESSERACT_LINUX

    def extract_text(self, image):
        return pytesseract.image_to_string(image, lang=StaticConstant.PYTESSERACT_LANGUANGE)