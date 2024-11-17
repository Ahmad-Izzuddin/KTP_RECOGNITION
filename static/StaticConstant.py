class StaticConstant:
    WEBCAM_ID = 0
    DELAY_OBJECT_DETECTION = 5
    PYTESSERACT_LANGUANGE = 'ocraext'
    OBJECT_CLASS_INDEX = 0
    DATE_FORMAT = "%d%m%Y%H%M%S"
    PREPROCESSED_IMG_TEMPLATE = "ktp_preprocessed_{}.jpg"
    EXTRACTED_TEXT_TEMPLATE = "ktp_preprocessed_{}.txt"
    DEFAULT_PLATFORM = "Windows"
    MODEL_TYPE = 'custom'
    DETECT_RESULT_TRUE = '\033[92mKTP detected in this frame\033[0m'
    DETECT_RESULT_FALSE = '\033[91mKTP not detected in this frame\033[0m'
    OUTPUT_IMAGE_FILE = f'\033[96mPreprocessed image saved: \033[0m'
    OUTPUT_TEXT_FILE = f'\033[96mExtracted text saved: \033[0m'
    WINDOW_WEBCAM_TITLE = 'Webcam'
    FAILED_OPEN_WEBCAM = 'Error: Could not open webcam'
    FAILED_TAKE_FRAME = 'Error: Could not take frame'
    BUTTON_CLOSE_WEBCAM = ' '