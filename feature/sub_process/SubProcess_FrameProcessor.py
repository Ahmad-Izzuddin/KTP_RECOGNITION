import cv2
from PIL import Image
from datetime import datetime

from static.StaticConstant import StaticConstant

class SubProcess_FrameProcessor:
    def __init__(self, model, image_processor, ocr_processor, output_handler):
        self.model = model
        self.image_processor = image_processor
        self.ocr_processor = ocr_processor
        self.output_handler = output_handler

    def process_frame(self, frame):
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        detected_objects = self.model.detect(img)
        
        for _, row in detected_objects.iterrows():
            if int(row['class']) == StaticConstant.OBJECT_CLASS_INDEX:
                print(StaticConstant.DETECT_RESULT_TRUE)
                xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                cropped_img = frame[ymin:ymax, xmin:xmax]
                processed_img = self.image_processor.preprocess(cropped_img)

                timestamp = datetime.now().strftime(StaticConstant.DATE_FORMAT)
                preprocessed_filename = f"{self.output_handler.preprocessing_output}/" + StaticConstant.PREPROCESSED_IMG_TEMPLATE.format(timestamp)
                extracted_text_filename = f"{self.output_handler.text_output}/" + StaticConstant.EXTRACTED_TEXT_TEMPLATE.format(timestamp)

                self.output_handler.save_image(processed_img, preprocessed_filename)
                extracted_text = self.ocr_processor.extract_text(processed_img)
                self.output_handler.save_text(extracted_text, extracted_text_filename)

                print(StaticConstant.OUTPUT_IMAGE_FILE + preprocessed_filename)
                print(StaticConstant.OUTPUT_TEXT_FILE + extracted_text_filename)

                return True
        print(StaticConstant.DETECT_RESULT_FALSE)
        return False