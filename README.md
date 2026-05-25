# 📄 ResumeBuddy — AI Resume Analyzer

An AI-powered resume analyzer built with Python & Flask. Upload your resume and instantly get your ATS score, matched/missing skills, and smart improvement suggestions.

🔗 **Live Demo:** [resumebuddy-3nc0.onrender.com/](https://resumebuddy-3nc0.onrender.com/)

---

## ✨ Features

- **ATS Score** — See how well your resume performs in Applicant Tracking Systems
- **Role Match %** — Check compatibility with your target job role
- **Skill Analysis** — View matched skills and identify missing ones instantly
- **Section Breakdown** — Get scores for Education, Skills, Projects, Experience & Certifications
- **AI Suggestions** — Receive actionable tips to improve your resume
- **PDF Report** — Download a full analysis report as a PDF
- **Resume Preview** — View extracted resume text directly in the dashboard

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| PDF Parsing | PyPDF2 / python-docx |
| PDF Report | ReportLab |
| Charts | Chart.js |
| Deployment | Render |

---

## 📸 Screenshots

> Dashboard with ATS Score, Skill Analysis & Charts

<img width="947" height="434" alt="Screenshot 2026-05-09 113841" src="https://github.com/user-attachments/assets/76a610f0-1bcc-46c2-94f4-28230c13b05b" />

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/resumebuddy.git
cd resumebuddy
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

---

## 📁 Project Structure

```
resumebuddy/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile                # For Render deployment
├── uploads/                # Temporary resume uploads
├── templates/
│   ├── index.html          # Landing page
│   └── dashboard.html      # Analysis dashboard
├── static/
│   ├── css/
│   │   └── style.css       # All styles
│   └── js/
│       └── script.js       # Frontend interactions
└── utils/
    ├── parser.py           # Resume text extraction
    ├── analyzer.py         # Skill matching & analysis
    └── scorer.py           # ATS score calculation
```

---

## 🎯 Supported Job Roles

- Frontend Developer
- Backend Developer
- Full Stack Developer
- Data Analyst
- Data Scientist
- UI/UX Designer

---

## 📦 Deployment

This app is deployed on **Render**. To deploy your own instance:

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Deploy!

---

## 🙋‍♀️ Author

**Shreya Meshram**  
[LinkedIn](https://www.linkedin.com/in/shreya-meshram28/) · [GitHub](https://github.com/meshramshreya28/ResumeBuddy)

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).
