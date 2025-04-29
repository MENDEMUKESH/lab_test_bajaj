

import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR"  # Update this path if necessary

def extract_text_from_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("L")
    text  = pytesseract.image_to_string(image)
    return text
