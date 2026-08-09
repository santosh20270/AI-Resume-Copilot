import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.skill_gap import analyze_skill_gap
from app.ui.skill_gap_dashboard import render_skill_gap_dashboard


def render_skill_gap():
    """
    Render the AI Skill Gap Dashboard page.
    """

    # =====================================================
    # Page Header
    # =====================================================

    st.title("📊 AI Skill Gap Dashboard")

    st.write(
        "Analyze your resume against a job description and discover "
        "missing skills, learning roadmap, recommended projects, "
        "and certifications."
    )

    st.divider()

    # =====================================================
    # Upload Section
    # =====================================================

    st.subheader("📂 Resume & Job Description")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown("### 📄 Resume")

            resume_file = st.file_uploader(
                "Upload your resume",
                type=[
                    "pdf",
                    "docx",
                    "txt",
                ],
                key="skill_resume",
            )

            if resume_file:

                st.success(
                    f"✓ {resume_file.name}"
                )

    with col2:

        with st.container(border=True):

            st.markdown("### 💼 Target Job")

            job_file = st.file_uploader(
                "Upload the job description",
                type=[
                    "pdf",
                    "docx",
                    "txt",
                ],
                key="skill_job",
            )

            if job_file:

                st.success(
                    f"✓ {job_file.name}"
                )

    st.divider()

    # =====================================================
    # Analyze Skill Gap
    # =====================================================

    if st.button(
        "📊 Analyze Skill Gap",
        use_container_width=True,
        type="primary",
    ):

        if resume_file is None:

            st.error(
                "Please upload your resume first."
            )

            st.stop()

        if job_file is None:

            st.error(
                "Please upload the target job description."
            )

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

        # -------------------------------------------------
        # Save Resume
        # -------------------------------------------------

        try:

            with open(
                resume_path,
                "wb",
            ) as f:

                f.write(
                    resume_file.getbuffer()
                )

        except Exception:

            st.error(
                "⚠️ Unable to save the uploaded resume. "
                "Please try again."
            )

            st.stop()

        # -------------------------------------------------
        # Save Job Description
        # -------------------------------------------------

        try:

            with open(
                job_path,
                "wb",
            ) as f:

                f.write(
                    job_file.getbuffer()
                )

        except Exception:

            st.error(
                "⚠️ Unable to save the job description. "
                "Please try again."
            )

            st.stop()

        # -------------------------------------------------
        # Extract Resume
        # -------------------------------------------------

        try:

            with st.spinner(
                "📄 Reading your resume..."
            ):

                resume_text = extract_text(
                    resume_path
                )

        except Exception:

            st.error(
                "⚠️ Unable to read your resume. "
                "Please check the file and try again."
            )

            st.stop()

        # -------------------------------------------------
        # Extract Job Description
        # -------------------------------------------------

        try:

            with st.spinner(
                "💼 Reading the job description..."
            ):

                job_description = extract_text(
                    job_path
                )

        except Exception:

            st.error(
                "⚠️ Unable to read the job description. "
                "Please check the file and try again."
            )

            st.stop()

        # -------------------------------------------------
        # AI Skill Gap Analysis
        # -------------------------------------------------

        try:

            with st.spinner(
                "🤖 AI is analyzing your skill gap..."
            ):

                report = analyze_skill_gap(
                    resume_text,
                    job_description,
                )

        except RuntimeError as error:

            st.error(
                str(error)
            )

            st.stop()

        except Exception:

            st.error(
                "⚠️ Something went wrong while analyzing "
                "your skill gap. Please try again."
            )

            st.stop()

        # -------------------------------------------------
        # Display Dashboard
        # -------------------------------------------------

        st.success(
            "✅ Skill Gap Analysis Completed!"
        )

        try:

            render_skill_gap_dashboard(
                report
            )

        except Exception:

            st.error(
                "⚠️ The skill gap report was generated, "
                "but the dashboard could not be displayed."
            )