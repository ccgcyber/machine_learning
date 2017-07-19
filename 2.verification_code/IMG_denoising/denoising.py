#coding:utf-8
import Image
import pytesseract
import ImageEnhance

img = Image.open('11.png')
img = img.convert('RGBA')
img = img.convert('L')
img.save('end_9.png')

sharpness = ImageEnhance.Sharpness(img)# Sharpened
img = sharpness.enhance(7.0)
img.save('end_0.png')
#img = ImageEnhance.Color(img) # Black and white
#img = img.enhance(0)
img.save('end_1.png')
#img = ImageEnhance.Brightness(img) # Increase brightness
#img = img.enhance(3)
img.save('end_2.png')
img = ImageEnhance.Contrast(img) # High contrast
img = img.enhance(8)
img.save('end_3.png')
#img = ImageEnhance.Color(img)
#img = img.convert('L')
