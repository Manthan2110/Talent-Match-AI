import os
from flask import Flask, request, render_template
from pypdf import PdfReader
from resumeparser import ats_extractor

UPLOAD_PATH = "__DATA__"
os.makedirs(UPLOAD_PATH, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
# app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Optional: 5 MB file limit

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def ats():
    if 'pdf_doc' not in request.files:
        return render_template('index.html', data={'error': "No file uploaded."})
    doc = request.files['pdf_doc']
    filename = "file.pdf"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    doc.save(filepath)
    data = _read_file_from_path(filepath)
    data = ats_extractor(data)
    return render_template('index.html', data=data)

def _read_file_from_path(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted.strip() + "\n"
    return text.strip()

if __name__ == "__main__":
    app.run(port=8000, debug=True)
