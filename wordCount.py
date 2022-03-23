import textract
import re


pdfFilePath = r"C:\Users\Usuario\Desktop\Antonio\coverletter\coverletterANtonioManceras2022.pdf"
pdfFilePath1 = r"C:\Users\Usuario\Desktop\Antonio\coverletter\pg996.epub"
pdfFilePath2 = r"C:\Users\Usuario\Desktop\Antonio\coverletter\potterfr.pdf"

def pdfToString(path):
  text = textract.process(path,encoding='ascii')
  textString=text.decode("utf-8")
  return textString


def arrayWords(text):
  arrayWords=text.split()
  return arrayWords

def arrayWordsLowerPdf(text):
  textStringLower=text.lower()
  arrayWords=re.findall(r"[\w']+", textStringLower)
  return arrayWords


def pdftoTextLower(text):
  textStringLower=text.lower()
  return textStringLower