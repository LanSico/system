import pytesseract
from PIL import Image

file='test.png'
image = Image.open(file)
code = pytesseract.image_to_string(image,lang='chi_sim')
print(code)
