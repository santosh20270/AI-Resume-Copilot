import os
import streamlit as st

from app.services.document_service import extract_text

# =====================================================
# AI Modules
# =====================================================

from app.ai.ats import analyze_resume

# =====================================================
# UI
# =====================================================

from app.ui.dashboard import render_dashboard
from app.ui.theme import load_theme
from app.ui.sidebar import render_sidebar

# =====================================================
# Pages
# =====================================================

from app.pages.resume_rewrite import render_resume_rewrite
from app.pages.cover_letter import render_cover_letter
from app.pages.interview_prep import render_interview_prep

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Resume Copilot",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------
# Load Theme
# ----------------------------------------------------

load_theme()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

page = render_sidebar()

# ====================================================
# ATS ANALYZER
# ====================================================

if page == "📄 ATS Analyzer":

    st.title("📄 AI Resume Copilot")

    st.subheader(
        "Analyze your resume against any job description using AI"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.header("📄 Resume")

        resume_file = st.file_uploader(
            "Upload Resume",
            type=["pdf", "docx", "txt", "png", "jpg", "jpeg"],
            key="resume",
        )

    with col2:

        st.header("💼 Job Description")

        job_file = st.file_uploader(
            "Upload Job Description",
            type=["pdf", "docx", "txt", "png", "jpg", "jpeg"],
            key="job",
        )

    st.divider()

    if st.button(
        "🚀 Analyze Resume",
        use_container_width=True,
    ):

        if resume_file is None:
            st.error("Please upload a Resume.")
            st.stop()

        if job_file is None:
            st.error("Please upload a Job Description.")
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

        with st.spinner("🤖 AI is analyzing your Resume..."):
            report = analyze_resume(
                resume_text,
                job_description,
            )

        render_dashboard(report)

# ====================================================
# RESUME REWRITE
# ====================================================

elif page == "📝 Resume Rewrite":

    render_resume_rewrite()

# ====================================================
# COVER LETTER
# ====================================================

elif page == "📨 Cover Letter":

    render_cover_letter()

# ====================================================
# INTERVIEW PREPARATION
# ====================================================

elif page == "🎤 Interview Prep":

    render_interview_prep()

# ====================================================
# SKILL GAP
# ====================================================

elif page == "📊 Skill Gap":

    st.title("📊 AI Skill Gap Analysis")

    st.info(
        "🚧 This feature will be available in Version 3.3"
    )

# ====================================================
# SETTINGS
# ====================================================

elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.subheader("AI Resume Copilot")

    st.write("Version : 3.2")

    st.write("Model : Gemini 3.6 Flash")

    st.write("Developer : Santosh")

    st.divider()

    st.success("✅ Application is running successfully.")