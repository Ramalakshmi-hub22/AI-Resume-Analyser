def calculate_ats_score(found_skills, required_skills):
    if len(required_skills) == 0:
        return 0

    matched_skills = 0

    for skill in required_skills:
        if skill in found_skills:
            matched_skills += 1

    score = (matched_skills / len(required_skills)) * 100

    return round(score, 2)