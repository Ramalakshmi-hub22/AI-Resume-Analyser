from utils.skill_extractor import extract_skills

def get_required_skills(job_description):
    """
    Extracts the required skills from the job description.
    """

    required_skills = extract_skills(job_description)

    return required_skills