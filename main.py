import pathlib
import warnings
import platform

from static.StaticConstant import StaticConstant

if platform.system() == StaticConstant.DEFAULT_PLATFORM:
    pathlib.PosixPath = pathlib.WindowsPath

warnings.simplefilter(action='ignore', category=FutureWarning)

from feature.WebcamCapture import WebcamCapture
from feature.YoloModel import YoloModel
from feature.ImageProcessor import ImageProcessor
from feature.OcrProcessor import OcrProcessor
from feature.OutputHandler import OutputHandler
from feature.Process import Process

def main():
    webcam = WebcamCapture()
    model = YoloModel()
    image_processor = ImageProcessor()
    ocr_processor = OcrProcessor()
    output_handler = OutputHandler()

    ktp_detection = Process(webcam, model, image_processor, ocr_processor, output_handler)
    ktp_detection.run()

if __name__ == "__main__":
    main()
