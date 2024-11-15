from feature.sub_process.SubProcess_DetectionTimer import SubProcess_DetectionTimer
from feature.sub_process.SubProcess_DisplayHandler import SubProcess_DisplayHandler
from feature.sub_process.SubProcess_FrameProcessor import SubProcess_FrameProcessor

class Process:
    def __init__(self, webcam, model, image_processor, ocr_processor, output_handler):
        self.webcam = webcam
        self.timer = SubProcess_DetectionTimer()
        self.processor = SubProcess_FrameProcessor(model, image_processor, ocr_processor, output_handler)
        self.display = SubProcess_DisplayHandler()

    def run(self):
        try:
            while True:
                frame = self.webcam.get_frame()
                if frame is None:
                    break

                if self.timer.is_time_to_detect():
                    self.processor.process_frame(frame)

                self.display.show_frame(frame)
                if self.display.is_exit_requested():
                    break

        finally:
            self.webcam.release()
            self.display.close()