import os
import pdfplumber
from pdf2docx import Converter

def pdf_to_txt(input_path):
    output_path = os.path.splitext(input_path)[0] + ".txt"

    lines = []

    with pdfplumber.open(input_path) as pdf:
        for page in pdf.pages:
            lines.append(page.extract_text())
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(lines))

    return output_path

def pdf_to_docx(input_path):
    output_path = os.path.splitext(input_path)[0] + ".docx"

    cv = Converter(input_path)
    cv.convert(output_path)
    cv.close()

    return output_path