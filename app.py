import os
from flask import Flask, render_template, request, send_file

# Importing converters
from converters.document_converters.pdf_converters import pdf_to_docx, pdf_to_txt
from converters.document_converters.docx_converters import docx_to_pdf, docx_to_txt
from converters.document_converters.txt_converters import txt_to_pdf, txt_to_docx

# Mapping input/output formats to conversion functions
converters = {
    ('pdf', 'docx'): pdf_to_docx,
    ('pdf', 'txt'): pdf_to_txt,
    ('docx', 'pdf'): docx_to_pdf,
    ('docx', 'txt'): docx_to_txt,
    ('txt', 'pdf'): txt_to_pdf,
    ('txt', 'docx'): txt_to_docx
}

# Initializing Flask app instance
app = Flask(__name__)

# Constants for where files are stored
UPLOADS_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'

# Create folders if they don't already exist
os.makedirs(UPLOADS_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# When visiting '/' index.html is shown to user
@app.route('/')
def index():
    return render_template('index.html')

# Run convert() when the form is submitted via POST
@app.route('/convert', methods=['POST'])
def convert():
    # Retrieving uploaded file and requested output format
    uploaded_file = request.files['file']
    input_format = request.form['input_format']
    output_format = request.form['output_format']

    if uploaded_file and input_format and output_format:
        input_path = os.path.join(UPLOADS_FOLDER, uploaded_file.filename)
        uploaded_file.save(input_path)

        key = (input_format, output_format)

        if key in converters:
            output_path = converters[key](input_path)
            return send_file(output_path, as_attachment=True)
        else:
            return f"Unsupported conversion: {key}", 400
    
    return "Invalid request", 400

# Run the app when executing python app.py
if __name__ == '__main__':
    app.run(debug=True)