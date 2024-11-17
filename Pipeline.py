import pathlib
import warnings
import platform

from static.StaticConstant import StaticConstant
from feature.WebcamCapture import WebcamCapture
from feature.YoloModel import YoloModel
from feature.ImageProcessor import ImageProcessor
from feature.OcrProcessor import OcrProcessor
from feature.OutputHandler import OutputHandler
from feature.Process import Process

class Pipeline:
    def __init__(self):
        # Platform-specific adjustments
        if platform.system() == StaticConstant.DEFAULT_PLATFORM:
            pathlib.PosixPath = pathlib.WindowsPath
        
        warnings.simplefilter(action='ignore', category=FutureWarning)

        # Initialize components
        self.webcam = WebcamCapture()
        self.model = YoloModel()
        self.image_processor = ImageProcessor()
        self.ocr_processor = OcrProcessor()
        self.output_handler = OutputHandler()

    def run(self):
        # Create and run the KTP detection process
        Process(
            self.webcam, 
            self.model, 
            self.image_processor, 
            self.ocr_processor, 
            self.output_handler
        ).run()
