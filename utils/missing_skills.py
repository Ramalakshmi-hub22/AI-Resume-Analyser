def get_missing_skills(found_skills, required_skills):
    missing = []

    for skill in required_skills:
        if skill not in found_skills:
            missing.append(skill)

    return missing