import cv2
import time
import numpy as np
import psutil
import os
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
        process = psutil.Process(os.getpid())

        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        start_detection_time = time.time()
        memory_before = process.memory_info().rss / 1024
        detected_objects = self.model.detect(img)
        memory_after = process.memory_info().rss / 1024
        detection_time = time.time() - start_detection_time

        detection_memory = f"Detection Memory: {memory_after - memory_before:.2f} KB\n"

        detection_time = f"Detection time: {detection_time}s\n"

        for _, row in detected_objects.iterrows():
            if int(row['class']) == StaticConstant.OBJECT_CLASS_INDEX:
                print(StaticConstant.DETECT_RESULT_TRUE)
                xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                cropped_img = frame[ymin:ymax, xmin:xmax]
                processed_img = self.image_processor.preprocess(cropped_img)

                confidence = row['confidence']
                confidence_text = f"Confidence: {confidence * 100:.2f}%\n"

                timestamp = datetime.now().strftime(StaticConstant.DATE_FORMAT)
                preprocessed_filename = f"{self.output_handler.preprocessing_output}/" + StaticConstant.PREPROCESSED_IMG_TEMPLATE.format(timestamp)
                text_filename = f"{self.output_handler.text_output}/" + StaticConstant.EXTRACTED_TEXT_TEMPLATE.format(timestamp)

                self.output_handler.save_image(processed_img, preprocessed_filename)
                start_extraction_time = time.time()
                memory_before = process.memory_info().rss / 1024
                output_text = self.ocr_processor.extract_text(processed_img)
                memory_after = process.memory_info().rss / 1024
                extraction_time = time.time() - start_extraction_time
                
                extraction_memory = f"Extraction Memory: {memory_after - memory_before:.2f} KB\n\n"

                extraction_time = f"Extraction time: {extraction_time}s\n"
                output_text = confidence_text + detection_time + detection_memory + extraction_time + extraction_memory + output_text
                self.output_handler.save_text(output_text, text_filename)

                lines = output_text.splitlines()
                if len(lines) >= 7:
                    line = lines[7]

                else:
                    line = "Baris NIK tidak tersedia."

                self.show_text_window(line)

                print(StaticConstant.OUTPUT_IMAGE_FILE + preprocessed_filename)
                print(StaticConstant.OUTPUT_TEXT_FILE + text_filename)
                return True
        print(StaticConstant.DETECT_RESULT_FALSE)
        return False

    def show_text_window(self, text):
        # Cari angka pertama dan ambil 16 karakter setelahnya
        start_index = -1
        for i, char in enumerate(text):
            if char.isdigit():
                start_index = i
                break

        if start_index != -1 and len(text) >= start_index + 16:
            extracted_text = text[start_index:start_index + 16]  # Ambil 16 karakter setelah angka pertama

            # Validasi apakah semua karakter adalah angka
            if all(c.isdigit() for c in extracted_text):
                text = extracted_text
            else:
                text = "Format tidak valid"
        else:
            text = "Format tidak valid"

        # Membuat gambar kosong untuk menampilkan teks
        window_width, window_height = 480, 320
        blank_image = np.zeros((window_height, window_width, 3), np.uint8)
        blank_image[:] = (255, 255, 255)  # Latar belakang putih

        # Menggambar teks pada gambar
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        color = (0, 0, 0)  # Warna teks hitam
        thickness = 1
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = (window_width - text_size[0]) // 2
        text_y = (window_height + text_size[1]) // 2

        cv2.putText(blank_image, text, (text_x, text_y), font, font_scale, color, thickness)

        # Menampilkan jendela
        cv2.imshow("Extracted Text - Line 4", blank_image)
        cv2.waitKey(3000)  # Tunggu selama 3 detik
        cv2.destroyAllWindows()

