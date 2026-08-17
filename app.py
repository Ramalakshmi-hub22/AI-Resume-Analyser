import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.missing_skills import get_missing_skills
from utils.jd_parser import get_required_skills
from utils.suggestions import generate_suggestions
from utils.report_generator import generate_report
from components.charts import create_skill_chart


# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Resume Analyser",
    page_icon="📄",
    layout="wide"
)

# ----------------------------
# Load CSS
# ----------------------------
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass

load_css("assets/style.css")
# ----------------------------
# Logo
# ----------------------------


# ----------------------------
# Project Title
# ----------------------------


st.markdown("""
### 🎯 Analyze your Resume with AI

Upload your resume, compare it with a Job Description, calculate the ATS score, identify missing skills, and receive AI-powered improvement suggestions.
""")

# ----------------------------
# Title
# ----------------------------
st.title("📄 AI Resume Analyser")
st.write("Upload your resume and compare it with a Job Description.")

# ----------------------------
# Job Description
# ----------------------------
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "Paste the Job Description Here",
        height=250
    )

with right_col:
    st.subheader("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Choose your Resume (PDF)",
        type=["pdf"]
    )

    st.info("Supported Format: PDF")

# ----------------------------
# Process Resume
# ----------------------------
if uploaded_file is not None:

    if job_description.strip() == "":
        st.warning("⚠ Please paste a Job Description first.")

    else:

        st.success("✅ Resume uploaded successfully!")

        # Extract Resume Text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Display Resume Text
        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

        # Extract Resume Skills
        found_skills = extract_skills(resume_text)

        # Extract Required Skills
        required_skills = get_required_skills(job_description)

        # Calculate ATS Score
        ats_score = calculate_ats_score(
            found_skills,
            required_skills
        )

        # Missing Skills
        missing_skills = get_missing_skills(
            found_skills,
            required_skills
        )

        # Suggestions
        suggestions = generate_suggestions(
            missing_skills,
            ats_score
        )

        # Statistics
        matched_skills = len(
            [skill for skill in found_skills if skill in required_skills]
        )

        total_required = len(required_skills)
        missing_count = len(missing_skills)

        # Create Pie Chart
        skill_chart = create_skill_chart(
            matched_skills,
            missing_count
        )
        # ----------------------------
        # Resume Statistics
        # ----------------------------
        # ----------------------------
# Resume Statistics
# ----------------------------

st.markdown("---")
st.subheader("📊 Resume Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📌 Required Skills",
        value=total_required
    )

with col2:
    st.metric(
        label="✅ Matched Skills",
        value=matched_skills
    )

with col3:
    st.metric(
        label="❌ Missing Skills",
        value=missing_count
    )

with col4:
    st.metric(
        label="🎯 ATS Score",
        value=f"{ats_score}%"
    )

st.markdown("---")

        # ----------------------------
        # Skill Match Chart
        # ----------------------------
        #   st.subheader("📈 Skill Match Chart")

st.plotly_chart(
            skill_chart,
            use_container_width=True
        )

        # ----------------------------
        # Skills Found
        # ----------------------------
       # ----------------------------
# Skills Found
# ----------------------------

st.markdown("---")
st.subheader("💡 Skills Found")

if found_skills:
    cols = st.columns(2)

    for i, skill in enumerate(found_skills):
        with cols[i % 2]:
            st.success(f"✅ {skill}")
else:
    st.warning("No skills were found in the resume.")

st.markdown("---")

        # ----------------------------
        # ATS Score
        # ----------------------------
st.subheader("📈 ATS Score")

st.progress(int(ats_score))
st.metric("Overall ATS Score", f"{ats_score}%")
        # ----------------------------
        # Missing Skills
        # ----------------------------
st.subheader("❌ Missing Skills")

if missing_skills:
            for skill in missing_skills:
                st.error(skill)
            else:
             st.success("🎉 Congratulations! Your resume matches all required skills.")

        # ----------------------------
        # Resume Improvement Suggestions
        # ----------------------------
            st.subheader("💡 Resume Improvement Suggestions")

            if suggestions:
              for suggestion in suggestions:
                st.info(suggestion)
            else:
             st.success("No suggestions. Your resume looks excellent!")
             st.subheader("🤖 AI Resume Review")
             
# Generate PDF Report
# ----------------------------
report_path = "resume_analysis_report.pdf"

generate_report(
    report_path,
    ats_score,
    found_skills,
    missing_skills,
    suggestions
)

st.success("✅ Resume Analysis Report Generated Successfully!")

# ----------------------------
# Download PDF Report
# ----------------------------
with open(report_path, "rb") as pdf_file:
    st.download_button(
        label="📥 Download Resume Analysis Report",
        data=pdf_file,
        file_name="Resume_Analysis_Report.pdf",
        mime="application/pdf"
    )