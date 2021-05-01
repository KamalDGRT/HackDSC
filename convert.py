from PIL import Image
from pytesseract import pytesseract
from googletrans import Translator
translator = Translator()
#path_to_tesseract = r"C:\Program Files\Tesseract-OCR"
#pytesseract.tesseract_cmd = path_to_tesseract

#filtering 
def Simplifier(text):
	string=""
	string=text.replace('%',' ')
	string=text.replace('/',' ')
	return string
	
	
def Text_convertor(img_,flag):
	img=Image.open(img_)
	if (flag):
		text_=pytesseract.image_to_string(img,lang='hin')
	else:
		text_=pytesseract.image_to_string(img)
	return text_


def English(string):
	value=translator.translate(string)
	return value.text
