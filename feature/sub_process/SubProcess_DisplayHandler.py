import cv2
from static.StaticConstant import StaticConstant
from feature.ImageProcessor import ImageProcessor

class SubProcess_DisplayHandler:
    def __init__(self):
        self.original_window_name = StaticConstant.WINDOW_ORIGINAL_FRAME_TITLE
        self.preprocessed_window_name = StaticConstant.WINDOW_PREPROCESSED_FRAME_TITLE
        self.image_processor = ImageProcessor()

    def show_frame(self, frame):
        preprocessed_frame = self.image_processor.preprocess(frame)
        cv2.imshow(self.original_window_name, frame)
        cv2.imshow(self.preprocessed_window_name, preprocessed_frame)

    def is_exit_requested(self):
        return cv2.waitKey(1) & 0xFF == ord(StaticConstant.BUTTON_CLOSE_WEBCAM)
    
    def show_blackscreen(self):
        image = cv2.imread('background/background_1.jpg')
        cv2.namedWindow("Black Screen", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Black Screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Black Screen", image)

    def close(self):
        cv2.destroyAllWindows()
