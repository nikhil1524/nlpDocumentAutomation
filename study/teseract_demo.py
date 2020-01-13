from PIL import Image
import pytesseract

img= Image.open("data/swedish.png")
img.load()
result=pytesseract.image_to_string(img,lang="swe")
print(result)
