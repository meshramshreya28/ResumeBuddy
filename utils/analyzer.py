def analyze_resume(resume_text, role_skills):

    matched_skills = []
    missing_skills = []

    text = resume_text.lower()

    # Skill matching
    for skill in role_skills:
        
        if skill.lower() in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
        
    # COMPATIBILITY SCORE
    if not role_skills:
        compatibility = 50
    else:
        compatibility = int(
            (len(matched_skills) / len(role_skills)) * 100
            )

    # -----------------------------
    # SECTION BREAKDOWN (NEW)
    # -----------------------------

    section_scores = {}

    section_scores['Education'] = 95 if 'b.tech' in text or 'degree' in text else 60
    
    section_scores['Skills'] = min(100, len(matched_skills) * 12)
    
    section_scores['Projects'] = 90 if 'github' in text or 'project' in text else 50
    
    section_scores['Experience'] = 85 if 'intern' in text or 'experience' in text else 40
    
    section_scores['Certifications'] = 80 if 'certification' in text else 35

    # Suggestions
    suggestions = []

    if len(missing_skills) > 0:
        suggestions.append("Add missing technical skills relevant to job role.")

    if 'project' not in text:
        suggestions.append("Add detailed project section with technologies used.")

    if 'experience' not in text:
        suggestions.append("Include internship or work experience.")

    if 'certification' not in text:
        suggestions.append("Add certifications to improve credibility.")

    if len(text) < 1000:
        suggestions.append("Resume is too short. Add more detailed content.")

    return {
        'matched_skills': matched_skills,
        'missing_skills': missing_skills,
        'compatibility': compatibility,
        'section_scores': section_scores,
        'suggestions': suggestions
    }