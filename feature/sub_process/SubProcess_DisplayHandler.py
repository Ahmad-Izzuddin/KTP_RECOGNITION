import cv2

from static.StaticConstant import StaticConstant

class SubProcess_DisplayHandler:
    def __init__(self, window_name=StaticConstant.WINDOW_WEBCAM_TITLE):
        self.window_name = window_name

    def show_frame(self, frame):
        cv2.imshow(self.window_name, frame)

    def is_exit_requested(self):
        return cv2.waitKey(1) & 0xFF == ord(StaticConstant.BUTTON_CLOSE_WEBCAM)

    def close(self):
        cv2.destroyAllWindows()