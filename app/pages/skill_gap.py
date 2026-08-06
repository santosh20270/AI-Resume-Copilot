import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.skill_gap import analyze_skill_gap
from app.ui.skill_gap_dashboard import render_skill_gap_dashboard


def render_skill_gap():

    st.title("📊 AI Skill Gap Dashboard")

    st.write(
        "Analyze your resume against a job description and discover "
        "missing skills, learning roadmap, recommended projects, and certifications."
    )

    st.divider()

    # =====================================================
    # Upload Section
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        resume_file = st.file_uploader(
            "📄 Upload Resume",
            type=["pdf", "docx", "txt"],
            key="skill_resume",
        )

    with col2:

        job_file = st.file_uploader(
            "💼 Upload Job Description",
            type=["pdf", "docx", "txt"],
            key="skill_job",
        )

    st.divider()

    # =====================================================
    # Analyze Skill Gap
    # =====================================================

    if st.button(
        "📊 Analyze Skill Gap",
        use_container_width=True,
    ):

        if resume_file is None:
            st.error("Please upload a resume.")
            st.stop()

        if job_file is None:
            st.error("Please upload a job description.")
            st.stop()

        os.makedirs("uploads", exist_ok=True)

        resume_path = os.path.join(
            "uploads",
            resume_file.name,
        )

        job_path = os.path.join(
            "uploads",
            job_file.name,
        )

        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())

        with open(job_path, "wb") as f:
            f.write(job_file.getbuffer())

        with st.spinner("📄 Reading Resume..."):
            resume_text = extract_text(resume_path)

        with st.spinner("💼 Reading Job Description..."):
            job_description = extract_text(job_path)

        with st.spinner("🤖 AI is analyzing your skill gap..."):
            report = analyze_skill_gap(
                resume_text,
                job_description,
            )

        st.success("✅ Skill Gap Analysis Completed!")

        render_skill_gap_dashboard(report)