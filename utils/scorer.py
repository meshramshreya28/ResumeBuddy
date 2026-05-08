def calculate_ats_score(resume_text, role_skills):

    score = 0

    matched_keywords = 0

    # FIX FOR CUSTOM ROLE
    if not role_skills:
        return 50

    # Keyword matching score
    for skill in role_skills:

        if skill.lower() in resume_text:
            matched_keywords += 1

    keyword_score = (
        matched_keywords / len(role_skills)
    ) * 70

    # Resume structure scoring
    structure_score = 0

    important_sections = [

        'education',
        'skills',
        'project',
        'experience'
    ]

    for section in important_sections:

        if section in resume_text:
            structure_score += 7.5

    # Final ATS score
    score = keyword_score + structure_score

    return round(score, 2)