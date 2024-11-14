import torch

from static.StaticPath import StaticPath

class YoloModel:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=StaticPath.PATH_MODEL)
    
    def detect(self, image):
        results = self.model(image)
        return results.pandas().xyxy[0]