import cv2
from static.StaticConstant import StaticConstant

class WebcamCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(StaticConstant.CAMERA_ID)
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            exit()
    
    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            return None
        return frame

    def release(self):
        self.cap.release()