import cv2

class SubProcess_DisplayHandler:
    def __init__(self, window_name="Webcam"):
        self.window_name = window_name

    def show_frame(self, frame):
        cv2.imshow(self.window_name, frame)

    def is_exit_requested(self):
        return cv2.waitKey(1) & 0xFF == ord('q')

    def close(self):
        cv2.destroyAllWindows()