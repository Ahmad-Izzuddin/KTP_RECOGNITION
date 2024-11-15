import time

from static.StaticConstant import StaticConstant

class SubProcess_DetectionTimer:
    def __init__(self):
        self.last_detection_time = time.time()

    def is_time_to_detect(self):
        current_time = time.time()
        if current_time - self.last_detection_time >= StaticConstant.DELAY_OBJECT_DETECTION:
            self.last_detection_time = current_time
            return True
        return False