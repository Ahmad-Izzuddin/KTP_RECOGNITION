import torch

from static.StaticPath import StaticPath
from static.StaticConstant import StaticConstant

class YoloModel:
    def __init__(self):
        self.model = torch.hub.load(StaticPath.OBJECT_DETECTION_ALGORITHM, StaticConstant.MODEL_TYPE, path=StaticPath.TRAIN_MODEL)
    
    def detect(self, image):
        results = self.model(image)
        return results.pandas().xyxy[0]