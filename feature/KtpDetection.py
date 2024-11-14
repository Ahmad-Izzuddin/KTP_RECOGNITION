import time
import cv2
from PIL import Image

from static.StaticConstant import StaticConstant

class KtpDetection:
    def __init__(self, webcam, model, image_processor, ocr_processor, output_handler):
        self.webcam = webcam
        self.model = model
        self.image_processor = image_processor
        self.ocr_processor = ocr_processor
        self.output_handler = output_handler
        self.last_detection_time = time.time()
    
    def run(self):
        try:
            while True:
                frame = self.webcam.get_frame()
                if frame is None:
                    break

                current_time = time.time()
                
                if current_time - self.last_detection_time >= StaticConstant.DELAY_OBJECT_DETECTION:
                    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                    detected_objects = self.model.detect(img)

                    ktp_detected = False
                    for _, row in detected_objects.iterrows():
                        if int(row['class']) == 0:
                            ktp_detected = True
                            print("KTP detected!")

                            xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                            cropped_img = frame[ymin:ymax, xmin:xmax]
                            processed_img = self.image_processor.preprocess(cropped_img)

                            preprocessed_filename = f"{self.output_handler.preprocessing_output}/ktp_preprocessed_{int(time.time())}.jpg"
                            extracted_text_filename = f"{self.output_handler.text_output}/ktp_preprocessed_{int(time.time())}.txt"
                            
                            self.output_handler.save_image(processed_img, preprocessed_filename)
                            extracted_text = self.ocr_processor.extract_text(processed_img)
                            self.output_handler.save_text(extracted_text, extracted_text_filename)

                            print(f"Preprocessed image saved: {preprocessed_filename}")
                            print(f"Extracted text saved: {extracted_text_filename}")
                            break

                    if not ktp_detected:
                        print("KTP not detected in this frame.")
                    
                    self.last_detection_time = current_time

                cv2.imshow("Webcam", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            self.webcam.release()
            cv2.destroyAllWindows()