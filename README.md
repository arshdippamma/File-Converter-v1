# 🗂️ File Converter Web App

A simple web-based file converter built with **Python (Flask)** that allows users to upload a file, select the input and desired output formats, and download the converted result. Currently supports converting between common document types such as `.pdf`, `.docx`, and `.txt`.

---

## 🚀 Features

- Upload a file and convert it to a different format
- Two-format dropdowns: input type and target type
- Dynamic output format selection based on input
- Clean, minimal HTML interface
- Fully modular converter functions
- Extendable for other formats (images, audio, etc.)

---

## 🔁 Supported Conversions

| From  | To     |
|-------|--------|
| PDF   | DOCX, TXT |
| DOCX  | PDF, TXT |
| TXT   | DOCX, PDF |

---

## 🧱 Tech Stack

- **Python 3.10+**
- **Flask**
- `python-docx`
- `docx2pdf`
- `pdf2docx`
- `pdfplumber`
- `fpdf`

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/file-converter.git
cd file-converter
