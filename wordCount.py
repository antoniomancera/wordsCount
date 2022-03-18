import textract


pdfFilePath = r"C:\Users\Usuario\Desktop\Antonio\coverletter\coverletterANtonioManceras2022.pdf"
pdfFilePath1 = r"C:\Users\Usuario\Desktop\Antonio\coverletter\pg996.epub"
pdfFilePath2 = r"C:\Users\Usuario\Desktop\Antonio\coverletter\potterfr.pdf"

def pdfToString(path):
  text = textract.process(path,encoding='ascii')
  textString=text.decode("utf-8")
  return textString


def arrayWords(text):
  # arrayWords=re.findall(r"[\w']+", textString)
  arrayWords=text.split()
  return arrayWords