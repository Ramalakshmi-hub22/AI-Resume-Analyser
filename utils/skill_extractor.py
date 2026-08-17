def extract_skills(resume_text):
    skills = [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",
        "React",
        "Node.js",
        "SQL",
        "MySQL",
        "MongoDB",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Artificial Intelligence",
        "Git",
        "GitHub",
        "DSA",
        "OOP"
    ]

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    return found_skills