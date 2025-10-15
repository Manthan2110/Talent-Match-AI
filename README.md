# 🧑‍💼 ResumeHub – AI-Powered Resume Parser & Matcher
*“Reading resumes is boring. Let AI do it for you.”* 🤖📄  
ResumeHub is your **AI-powered recruiting assistant** that extracts structured data from resumes **and** matches resumes against job descriptions with advanced AI. Built with 🧠 Google Gemini, 🖥️ Flask, and 🎨 TailwindCSS, it helps recruiters and candidates alike to parse, score, and improve resumes faster than ever.  

---

## 🧠 Problem Statement  
Recruiters spend hours parsing resumes and manually shortlisting candidates. This process is **slow, error-prone, and resource-intensive.**  
> ❓ *“Can resume screening and matching be automated with AI?”*  
> ✅ *Answer: Yes, with ResumeHub.*

---

## 🌐 Website Preview  
Home Page:
<img width="1918" height="1012" alt="image" src="https://github.com/user-attachments/assets/4cb4610c-a4a9-4e1d-8875-05020daba780" />

Parsing Page:
<img width="1918" height="992" alt="image" src="https://github.com/user-attachments/assets/cb993160-d6f2-4ff7-a66b-b11c50e7e47c" />

Resume Matcher Page:
<img width="1891" height="993" alt="image" src="https://github.com/user-attachments/assets/1a79487e-7003-4c04-8b78-bd06636666cf" />

---

## 📦 Features  
- 📄 **Resume Upload & Parsing** – Extracts structured details (personal info, education, experience, skills) from PDFs, DOCX, TXT  
- 🤖 **AI-Powered Parsing** – Uses Google Gemini for accurate and fast extraction  
- 👥 **Resume Matching** – Match multiple resumes against job descriptions using TF-IDF and AI semantic similarity  
- 🔎 **Missing Keywords Detection** – Highlights job description keywords missing from the resumes  
- 💡 **AI Improvement Suggestions** – Provides actionable tips to strengthen resume content  
- 📜 **Clean UI** – Modern responsive interface with TailwindCSS and real-time feedback  

---

## 🏗️ User Flow  



```text
User ➡️ Flask App ➡️ ResumeParser (Gemini) ➡️ JSON Output  
                   ⬇️            ⬆️                   ⬇️
          Resume Matching      PDF Upload          Structured Insights
```


---

## Project Files

| File                    | Description                                   |
|-------------------------|-----------------------------------------------|
| `app.py`                | Flask app with resume parse & matcher routes  |
| `resumeparser.py`       | AI-powered resume parsing logic                |
| `templates/*.html`      | Frontend UI built with TailwindCSS + Jinja2  |
| `static/`               | Static assets like CSS, images                  |
| `config.yaml`           | Stores Gemini API key  (ignored in git)       |
| `requirements.txt`      | Python dependencies                            |
| `__DATA__/`             | Directory for uploaded resumes                 |

---

## 🔐 Technologies Used

- 🧠 AI engine: Google Gemini (google-generativeai)  
- 🖥️ Backend: Flask  
- 📄 PDF Parsing: PyPDF, PyPDF2  
- 🖥️ NLP: sklearn TF-IDF, cosine similarity, custom keyword extraction  
- 🎨 Frontend: TailwindCSS, Jinja2 Templates  
- ⚙️ Config & Env: PyYAML, python-dotenv  

---

## 🚀 Installation & Setup


### 1️⃣ Clone repo
```bash
git clone https://github.com/Manthan2110/Talent-Match-AI.git
cd Talent-Match-AI
```

### 2️⃣ Create virtual env & activate
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add in config.yaml
```bash
GEMINI_API_KEY: your_api_key_heree"
```
## 5️⃣ Run server
```bash
python app.py
```
👉 Visit http://localhost:8000

--- 

## 🖼️ Sample Output

```json
{
  "personal_info": {
    "full_name": "John Doe",
    "email": "john.doe@gmail.com",
    "phone": "+91 9876543210",
    "linkedin": "https://linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe"
  },
  "education": [
    {"degree": "B.Tech in CSE", "institution": "IIT Delhi", "year": "2023"}
  ],
  "experience": [
    {"role": "Software Engineer", "company": "Google", "start_date": "2023", "end_date": "Present"}
  ],
  "technical_skills": ["Python", "Flask", "React", "SQL"]
}
```


---

## 📈 How It Works (High Level)

- User uploads resume(s) and provides job description text  
- Flask backend extracts raw text and parses structured data via Gemini AI  
- Extracted data is vectorized with TF-IDF for cosine similarity matching  
- Matching resumes are ranked with percentage scores  
- Missing keywords from job description vs resume skills detected  
- AI generates improvement suggestions (currently static prototype)  
- Results and insights displayed with visual progress bars and highlights  

---

## 🎯 Future Enhancements

| Feature                     | Description                                    |
|-----------------------------|------------------------------------------------|
| 📊 ATS Score Computation    | Calculate precise resume-job fit scores        |
| 🌎 Multi-language Parsing   | Support parsing resumes in multiple languages  |
| 🧠 Transformer Embeddings   | Use semantic embeddings (e.g. SBERT) for matching |
| 📊 Recruiter Dashboard      | Analytics about candidates and hiring funnels  |
| ✉️ Interview Scheduling     | Coordinate scheduling and feedback per candidate |
| 🤝 Collaborative Review     | Allow multiple users to comment on resumes      |
| 🔎 Job Recommendations      | Suggest jobs to candidates based on skills      |

---

## 👨‍💻 Author

Made with 💼 and ❤️ by Manthan Jadav  
- [LinkedIn](https://www.linkedin.com/in/manthanjadav/)  
- 📧 Email: manthanjadav746@gmail.com

---

## 📜 License

This project is licensed under the MIT License.  
Parse freely. Fork happily. Contribute generously! 😄
