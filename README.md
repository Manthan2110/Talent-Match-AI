# 🧑‍💼 Talent-Match-AI – AI-Powered Resume Parser  

*“Reading resumes is boring. Let AI do it for you.”* 🤖📄  

Talent-Match-AI is your **AI-powered recruiter’s assistant** that extracts structured data from resumes in **seconds**. Built with 🧠 Google Gemini, 🖥️ Flask, and 🎨 TailwindCSS, it helps you parse PDFs into clean JSON and human-friendly summaries.  

---

## 🧠 Problem Statement  

Recruiters and HR teams spend **hours** manually scanning resumes for skills, experience, and education. This is **tedious, error-prone, and slow**.  

> ❓ *“Can we make resume screening as easy as uploading a file?”*  
> ✅ *Answer: Yes. Talent-Match-AI can.*  

---

## 🌐 Website Preview  
<img width="1913" height="1012" alt="image" src="https://github.com/user-attachments/assets/953b2579-bff8-4649-bb0e-2c247c8b7381" />

### Structured Summary
<img width="1918" height="1017" alt="image" src="https://github.com/user-attachments/assets/a3f8bada-d0b4-4c34-86f0-4438f1ddc90d" />



---

## 📦 Features  

- 📄 **PDF Resume Upload** – Drag, drop, done.  
- 🤖 **AI-Powered Parsing** – Uses Google Gemini for accurate data extraction.  
- 👤 **Personal Info Extraction** – Name, email, phone, LinkedIn, GitHub, location.  
- 🎓 **Education & Experience** – Degrees, roles, companies, and timelines.  
- 💡 **Skills & Projects** – Technical skills, frameworks, tools, and key projects.  
- 📜 **Certifications & Extras** – Courses, awards, and achievements.  
- 🎨 **Modern UI** – Clean TailwindCSS layout with instant feedback.  

---

## 🏗️ User Flow  

```text
User ➡️ Flask App ➡️ ResumeParser (Gemini) ➡️ JSON Output  
                                ⬆️                   ⬇️
                            PDF Upload          Structured Insights
```

---
## Project Files

| File                   | Description                                   |
| ---------------------- | --------------------------------------------- |
| `app.py`               | Flask app entry point (routes & server setup) |
| `resumeparser.py`      | AI-powered resume parsing logic               |
| `templates/index.html` | TailwindCSS-powered UI                        |
| `config.yaml`          | Stores Gemini API key (ignored in git)        |
| `requirements.txt`     | Python dependencies                           |
| `__DATA__/`            | Uploaded resumes directory                    |

---

## 🔐 Technologies Used
- 🧠 AI Model: Google Gemini (google-generativeai)
- 🖥️ Backend: Flask
- 📄 PDF Processing: PyPDF
- ⚙️ Config: PyYAML
- 🎨 Frontend: TailwindCSS + Jinja2

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

## Future Enhancement

| Feature                       | Description                            |
| ----------------------------- | -------------------------------------- |
| 📊 **ATS Score**              | Rate resumes against job descriptions  |
| 🌍 **Multi-language Support** | Parse resumes in Hindi, French, etc.   |
| 🧠 **NER Fine-Tuning**        | Custom ML for better field accuracy    |
| 📈 **Recruiter Dashboard**    | Visual analytics of parsed resumes     |
| 🔎 **Job Matching**           | Suggest jobs based on extracted skills |

---

## 👨‍💻 Author

- Made with 💼 and ❤️ by Manthan Jadav
- 📫 LinkedIn[https://www.linkedin.com/in/manthanjadav/]
-  ✉️ manthanjadav746@gmail.com[mailto:manthanjadav746@gmail.com]
  
---

## 📜 License
This project is licensed under the MIT License.
Parse freely. Fork happily. Contribute generously. 😄
