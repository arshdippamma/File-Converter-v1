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

Support for file format conversions for data, archive, images, videos, and audio file formats to be implemented.

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
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

You can also install manually:
```bash
pip install flash python-docx docx2pdf pdf2docx pdfplumber fpdf
```

### 4. Run the app

```bash
python app.py
```

Then visit: https://127.0.0.1:5000/

## 🗂️ Project Structure

```
file-converter/
├── app.py
├── templates/
│   └── index.html
├── converters/
│   ├── document_converters/
│   │   ├── pdf_converters.py
│   │   ├── docx_converters.py
│   │   └── txt_converters.py
├── uploads/
├── converted/
└── README.md
```

Note: the `uploads/` and `converted/` folders will be created by the application and are, therefore, excluded from this repo.

## 📌 Notes

- Only valid input/output format combinations are allowed via dropdowns.
- This is a local app — files are not stored or sent externally.
- Designed for educational/demo use; not secure for production without enhancements.

## 📄 License

MIT License. Feel free to modify, improve, and share.

## 🙌 Acknowledgments

- [Flask](https://flask.palletsprojects.com/en/stable/)
- [python-docx](https://github.com/python-openxml/python-docx)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [fpdf2](https://github.com/py-pdf/fpdf2)
