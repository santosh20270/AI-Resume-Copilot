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

from app.pages.home import render_home
from app.pages.resume_rewrite import render_resume_rewrite
from app.pages.cover_letter import render_cover_letter
from app.pages.interview_prep import render_interview_prep
from app.pages.skill_gap import render_skill_gap
from app.pages.settings import render_settings


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="AI Resume Copilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =====================================================
# Load Theme
# =====================================================

load_theme()


# =====================================================
# Navigation State
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"


# =====================================================
# Sidebar
# =====================================================

render_sidebar()

page = st.session_state.page


# =====================================================
# HOME
# =====================================================

if page == "🏠 Home":

    render_home()


# =====================================================
# ATS ANALYZER
# =====================================================

elif page == "📄 ATS Analyzer":

    st.title("📄 ATS Resume Analyzer")

    st.write(
        "Analyze your resume against a job description using AI."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        resume_file = st.file_uploader(
            "📄 Upload Resume",
            type=[
                "pdf",
                "docx",
                "txt",
                "png",
                "jpg",
                "jpeg",
            ],
            key="resume",
        )

    with col2:

        job_file = st.file_uploader(
            "💼 Upload Job Description",
            type=[
                "pdf",
                "docx",
                "txt",
                "png",
                "jpg",
                "jpeg",
            ],
            key="job",
        )

    st.divider()

    if st.button(
        "🚀 Analyze Resume",
        use_container_width=True,
    ):

        if resume_file is None:

            st.error("Please upload a resume.")
            st.stop()

        if job_file is None:

            st.error("Please upload a job description.")
            st.stop()

        os.makedirs(
            "uploads",
            exist_ok=True,
        )

        resume_path = os.path.join(
            "uploads",
            resume_file.name,
        )

        job_path = os.path.join(
            "uploads",
            job_file.name,
        )

        with open(
            resume_path,
            "wb",
        ) as f:

            f.write(
                resume_file.getbuffer()
            )

        with open(
            job_path,
            "wb",
        ) as f:

            f.write(
                job_file.getbuffer()
            )

        with st.spinner(
            "📄 Reading Resume..."
        ):

            resume_text = extract_text(
                resume_path
            )

        with st.spinner(
            "💼 Reading Job Description..."
        ):

            job_description = extract_text(
                job_path
            )

        with st.spinner(
            "🤖 AI is analyzing your resume..."
        ):

            report = analyze_resume(
                resume_text,
                job_description,
            )

        render_dashboard(report)


# =====================================================
# RESUME REWRITE
# =====================================================

elif page == "📝 Resume Rewrite":

    render_resume_rewrite()


# =====================================================
# COVER LETTER
# =====================================================

elif page == "📨 Cover Letter":

    render_cover_letter()


# =====================================================
# INTERVIEW PREPARATION
# =====================================================

elif page == "🎤 Interview Prep":

    render_interview_prep()


# =====================================================
# SKILL GAP
# =====================================================

elif page == "📊 Skill Gap":

    render_skill_gap()


# =====================================================
# SETTINGS
# =====================================================

elif page == "⚙️ Settings":

    render_settings()