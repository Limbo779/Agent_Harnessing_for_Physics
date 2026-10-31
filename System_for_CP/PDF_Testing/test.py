import pytesseract
from PIL import Image
from pix2text import Pix2Text

# 1. Define custom Tesseract wrapper function for P2T
def tesseract_text_ocr(img: Image.Image, **kwargs) -> str:
    # --psm 6 treats the crop box as a uniform block of text
    return pytesseract.image_to_string(img, config='--psm 6').strip()

# 2. Initialize Pix2Text with formula recognition
p2t = Pix2Text.from_config()

# 3. Override the default text recognition method with Tesseract
p2t.recognize_text = tesseract_text_ocr

# 4. Run layout-aware extraction
doc = p2t.recognize_pdf("/home/limbo/Desktop/Coding fun/Side (& fun) Projects/Agent Harness/System_for_CP/PDF_Testing/test_page.pdf", page_numbers=[0])
doc.save_markdown("output_p2t", page_images=True)