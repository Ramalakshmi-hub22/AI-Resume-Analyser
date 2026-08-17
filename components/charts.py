import plotly.express as px

def create_skill_chart(matched_skills, missing_skills):
    labels = ["Matched Skills", "Missing Skills"]
    values = [matched_skills, missing_skills]

    fig = px.pie(
        names=labels,
        values=values,
        title="Skill Match Analysis"
    )

    fig.update_traces(textinfo="percent+label")

    return fig