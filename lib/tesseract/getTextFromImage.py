import PIL
from PIL import Image
import pytesseract

def getTestFromImage(img)->str:
    return pytesseract.image_to_string(img, lang="ben")   