import cv2
from static.StaticConstant import StaticConstant

class WebcamCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(StaticConstant.WEBCAM_ID)
        if not self.cap.isOpened():
            print(StaticConstant.FAILED_OPEN_WEBCAM)
            exit()
    
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print(StaticConstant.FAILED_TAKE_FRAME)
            return None
        return frame

    def release(self):
        self.cap.release()