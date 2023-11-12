from pdfminer.high_level import extract_text
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser

page_number = 2

with open("HR01_J_syousai.pdf", "rb") as f:
    test      = extract_text(f, page_numbers=[page_number])


print(text)
print(type(text))
