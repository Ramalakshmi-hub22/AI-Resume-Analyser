def generate_suggestions(missing_skills, ats_score):
    suggestions = []

    if ats_score >= 90:
        suggestions.append("Excellent resume! Your resume matches the job description very well.")
        return suggestions

    if len(missing_skills) > 0:
        suggestions.append("Add the missing skills relevant to the job description.")

        for skill in missing_skills:
            suggestions.append(f"Include {skill} if you have experience with it.")

    suggestions.append("Write a strong professional summary.")
    suggestions.append("Quantify your achievements using numbers.")
    suggestions.append("Mention your projects clearly.")
    suggestions.append("Keep your resume to one page if possible.")
    suggestions.append("Proofread your resume for grammar and spelling mistakes.")

    return suggestions