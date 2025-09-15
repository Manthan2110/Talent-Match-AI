import os
from flask import Flask, request, render_template, redirect, url_for
import re
from pypdf import PdfReader
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from resumeparser import ats_extractor

UPLOAD_PATH = "__DATA__"
MATCH_UPLOAD_PATH = "uploads"
os.makedirs(UPLOAD_PATH, exist_ok=True)
os.makedirs(MATCH_UPLOAD_PATH, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
app.config['MATCH_UPLOAD_FOLDER'] = MATCH_UPLOAD_PATH

# Helper functions for resume matching
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except:
        # Fallback to pypdf if PyPDF2 fails
        reader = PdfReader(file_path)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted.strip() + "\n"
    return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return ""

def _read_file_from_path(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted.strip() + "\n"
    return text.strip()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/parser')
def parser():
    return render_template('parser.html')

@app.route('/matcher')
def matcher_page():
    return render_template('matcher.html')

@app.route('/process', methods=['POST'])
def process_resume():
    if 'pdf_doc' not in request.files:
        return render_template('parser.html', data={'error': "No file uploaded."})
    
    doc = request.files['pdf_doc']
    if doc.filename == '':
        return render_template('parser.html', data={'error': "No file selected."})
    
    filename = "file.pdf"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    doc.save(filepath)
    
    try:
        data = _read_file_from_path(filepath)
        data = ats_extractor(data)
        return render_template('parser.html', data=data)
    except Exception as e:
        return render_template('parser.html', data={'error': f"Error processing file: {str(e)}"})
    
def extract_keywords(text):
    # Simple tokenization + stopwords removal, or use spaCy/RAKE
    tokens = text.lower().split()
    stopwords = set([...])  # your stopwords list
    keywords = [t for t in tokens if t.isalpha() and t not in stopwords]
    return set(keywords)

# Add a simple stopwords list or import from nltk etc.
STOPWORDS = {
    "and", "or", "the", "for", "with", "a", "an", "of", "to", "in", "on", "by", "at", 
    "from", "as", "is", "are", "be", "will", "was", "were", "that", "this"
}

def extract_keywords(text):
    # Basic preprocessing: tokenize, lowercase, filter non-alphabetic and stopwords
    tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    keywords = {t for t in tokens if t not in STOPWORDS}
    return keywords

def aggregate_resume_keywords(parsed_data_list):
    # Collect skills, certifications, soft_skills, projects, etc., from parsed resume dictionaries
    keywords = set()
    for data in parsed_data_list:
        technical_skills = data.get("technical_skills", {})
        for cat, skill_list in technical_skills.items():
            keywords.update(kw.lower() for kw in skill_list if isinstance(kw, str))

        for field in ["soft_skills", "certifications", "projects"]:
            items = data.get(field)
            if items:
                if isinstance(items, list):
                    for item in items:
                        if isinstance(item, dict):
                            keywords.update(kw.lower() for kw in item.values() if isinstance(kw, str))
                        elif isinstance(item, str):
                            keywords.add(item.lower())
                elif isinstance(items, str):
                    keywords.add(items.lower())

    return keywords


@app.route('/match_resumes', methods=['POST'])
def match_resumes():
    job_description = request.form.get('job_description', '').strip()
    resume_files = request.files.getlist('resumes')

    if not job_description:
        return render_template('matcher.html', error="Please enter a job description.", job_description=job_description)

    if not resume_files or len(resume_files) < 1:
        return render_template('matcher.html', error="Please upload at least one resume.", job_description=job_description)

    resumes = []
    valid_files = []
    resumes_parsed_data = []

    for resume_file in resume_files:
        if resume_file.filename:
            filename = os.path.join(app.config['MATCH_UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filename)
            extracted_text = extract_text(filename)
            extracted_text = str(extracted_text).strip()
            if extracted_text:
                resumes.append(extracted_text)
                valid_files.append(resume_file.filename)

                # Parse resume text for keywords extraction (reuse your ats_extractor)
                try:
                    parsed_data = ats_extractor(extracted_text)
                    resumes_parsed_data.append(parsed_data)
                except Exception as e:
                    # For robustness, skip on parse errors
                    resumes_parsed_data.append({})

    if not resumes:
        return render_template('matcher.html', error="No valid text could be extracted from uploaded files.", job_description=job_description)

    try:
        vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
        vectors = vectorizer.fit_transform([job_description] + resumes)

        job_vector = vectors[0]
        resume_vectors = vectors[1:]
        similarities = cosine_similarity(job_vector, resume_vectors)[0]

        num_results = min(5, len(similarities))
        top_indices = similarities.argsort()[-num_results:][::-1]

        results = []
        for i in top_indices:
            results.append({
                'filename': valid_files[i],
                'score': round(similarities[i] * 100, 1)
            })

        job_keywords = extract_keywords(job_description)
        resume_keywords = aggregate_resume_keywords(resumes_parsed_data)
        missing_keywords = sorted(list(job_keywords - resume_keywords))

        # Placeholder: Simulate improvement suggestions (replace this with Gemini API call)
        improvement_suggestions = "Add more skills like TensorFlow, PyTorch, and Cloud Computing to improve your resume's visibility."

        return render_template(
            'matcher.html',
            results=results,
            job_description=job_description,
            missing_keywords=missing_keywords,
            improvement_suggestions=improvement_suggestions,
            total_resumes=len(valid_files)
        )

    except Exception as e:
        return render_template('matcher.html', error=f"Error processing resumes: {str(e)}", job_description=job_description)

    # return redirect(url_for('matcher_page'))


if __name__ == "__main__":
    app.run(port=8000, debug=True)