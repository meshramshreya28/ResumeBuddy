from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from utils.parser import extract_text
from utils.analyzer import analyze_resume
from utils.scorer import calculate_ats_score

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf', 'docx'}

latest_report = {}

# Job role skills database
ROLE_SKILLS = {
    'Frontend Developer': [
        'html', 'css', 'javascript', 'react',
        'tailwind', 'bootstrap', 'responsive design'
    ],

    'Backend Developer': [
        'python', 'flask', 'django', 'sql',
        'mongodb', 'api', 'mysql'
    ],

    'Full Stack Developer': [
        'html', 'css', 'javascript', 'react',
        'python', 'flask', 'mongodb', 'mysql'
    ],

    'Data Analyst': [
        'python', 'excel', 'power bi',
        'sql', 'tableau'
    ],

    'Data Scientist': [
        'machine learning', 'python',
        'tensorflow', 'numpy', 'pandas'
    ],

    'UI/UX Designer': [
        'figma', 'wireframe',
        'prototype', 'user research'
    ]
}
def calculate_section_score(resume_text, keywords, weight=1.0):
    text = resume_text.lower()
    found = sum(1 for kw in keywords if kw in text)
    base = round((found / len(keywords)) * 100) if keywords else 50
    return min(100, int(base * weight))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    if 'resume' not in request.files:
        return 'No file uploaded'

    file = request.files['resume']
    role = request.form.get('role', '').strip().title()

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        file.save(filepath)

        # Extract text from resume
        resume_text = extract_text(filepath)
        
        role_skills = ROLE_SKILLS.get(role, [])
        
        analysis = analyze_resume(
            resume_text,
            role_skills
            )
        
        ats_score = calculate_ats_score(
            resume_text,
            role_skills
            )
        
        # Generic suggestions when no role is entered
        if not role:
            
            analysis['suggestions'].append(
                'Add more measurable achievements and project details.'
                )
            
            analysis['suggestions'].append(
                'Include technical skills relevant to your target industry.'
                )
            
            analysis['suggestions'].append(
                'Use strong action verbs and ATS-friendly formatting.'
                )
               
        # Store latest report data
        global latest_report
        latest_report = {
            
            'ats_score': ats_score,
            
            'matched_skills': analysis['matched_skills'],
            
            'missing_skills': analysis['missing_skills'],
            
            'suggestions': analysis['suggestions'],
            
            'compatibility': analysis['compatibility'],
            
            'role': role
            }
        
        return render_template(
            
            'dashboard.html',
            
            ats_score=ats_score,
            
            matched_skills=analysis['matched_skills'],
            
            missing_skills=analysis['missing_skills'],
            
            suggestions=analysis['suggestions'],
            
            compatibility=analysis['compatibility'],
            
            section_scores={
    'Education': calculate_section_score(resume_text, [
        'bachelor', 'master', 'degree', 'university', 'college',
        'gpa', 'b.tech', 'b.sc', 'engineering', 'graduated'
    ]),
    'Skills': calculate_section_score(resume_text, [
        'python', 'javascript', 'sql', 'react', 'html', 'css',
        'machine learning', 'flask', 'django', 'git', 'java', 'c++'
    ]),
    'Projects': calculate_section_score(resume_text, [
        'project', 'built', 'developed', 'deployed', 'github',
        'created', 'implemented', 'designed', 'app', 'website'
    ]),
    'Experience': calculate_section_score(resume_text, [
        'experience', 'internship', 'worked', 'company', 'role',
        'position', 'responsibilities', 'team', 'led', 'managed'
    ]),
    'Certifications': calculate_section_score(resume_text, [
        'certification', 'certified', 'certificate', 'coursera',
        'udemy', 'aws', 'google', 'microsoft', 'credential', 'badge'
    ]),
},

    resume_text=resume_text[:2000],

    role=role
)

    return 'Invalid file type'

@app.route('/download-report')
def download_report():

    import uuid
    
    pdf_file = f"resume_report_{uuid.uuid4().hex}.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        'ResumeBuddy Analysis Report',
        styles['Title']
    )

    content.append(title)

    content.append(Spacer(1, 20))

    # ATS Score
    ats = Paragraph(
        f"ATS Score: {latest_report['ats_score']}%",

        styles['Heading2']
    )

    content.append(ats)

    # Compatibility
    compatibility = Paragraph(

        f"Role Match: {latest_report['compatibility']}%",

        styles['Heading2']
    )

    content.append(compatibility)

    content.append(Spacer(1, 20))

    # Matched Skills
    matched = Paragraph(

        'Matched Skills: ' +

        ', '.join(latest_report['matched_skills']),

        styles['BodyText']
    )

    content.append(matched)

    content.append(Spacer(1, 12))

    # Missing Skills
    missing = Paragraph(

        'Missing Skills: ' +

        ', '.join(latest_report['missing_skills']),

        styles['BodyText']
    )

    content.append(missing)

    content.append(Spacer(1, 20))

    # Suggestions
    suggestions = Paragraph(

        'Suggestions:<br/><br/>' +

        '<br/>'.join(latest_report['suggestions']),

        styles['BodyText']
    )

    content.append(suggestions)

    doc.build(content)

    return send_file(

        pdf_file,

        as_attachment=True
    )
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "ResumeBuddy is running 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)