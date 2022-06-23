import imghdr
from PIL import Image
import pytesseract 

#모든 텍스트 출력

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

img = Image.open('c:/PythonWorkspace/text_from_img/imgtest/test1.jpg')

text = pytesseract.image_to_string(img)

print (text.strip())
