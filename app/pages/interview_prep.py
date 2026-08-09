import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.interview import generate_interview_questions


def render_interview_prep():
    """
    Render the AI Interview Preparation page.
    """

    # =====================================================
    # Page Header
    # =====================================================

    st.title("🎤 AI Interview Preparation")

    st.write(
        "Prepare for your target role with AI-generated "
        "technical, HR, and behavioral interview questions."
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
                key="interview_resume",
            )

            if resume_file:

                st.success(
                    f"✓ {resume_file.name}"
                )

    with col2:

        with st.container(border=True):

            st.markdown("### 💼 Target Job")

            jd_file = st.file_uploader(
                "Upload the job description",
                type=[
                    "pdf",
                    "docx",
                    "txt",
                ],
                key="interview_jd",
            )

            if jd_file:

                st.success(
                    f"✓ {jd_file.name}"
                )

    st.divider()

    # =====================================================
    # Generate Interview Preparation
    # =====================================================

    if st.button(
        "🚀 Generate Interview Preparation",
        use_container_width=True,
        type="primary",
    ):

        if resume_file is None:

            st.error(
                "Please upload your resume first."
            )

            st.stop()

        if jd_file is None:

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

        jd_path = os.path.join(
            "uploads",
            jd_file.name,
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
                jd_path,
                "wb",
            ) as f:

                f.write(
                    jd_file.getbuffer()
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

                jd_text = extract_text(
                    jd_path
                )

        except Exception:

            st.error(
                "⚠️ Unable to read the job description. "
                "Please check the file and try again."
            )

            st.stop()

        # -------------------------------------------------
        # Generate Interview Guide
        # -------------------------------------------------

        try:

            with st.spinner(
                "🤖 AI is preparing your interview guide..."
            ):

                report = generate_interview_questions(
                    resume_text,
                    jd_text,
                )

        except RuntimeError as error:

            st.error(
                str(error)
            )

            st.stop()

        except Exception:

            st.error(
                "⚠️ Something went wrong while generating "
                "your interview preparation. Please try again."
            )

            st.stop()

        # -------------------------------------------------
        # Store Result
        # -------------------------------------------------

        st.session_state[
            "interview_report"
        ] = report

        st.session_state[
            "interview_complete"
        ] = True

        st.rerun()

    # =====================================================
    # Interview Results
    # =====================================================

    if st.session_state.get(
        "interview_complete",
        False,
    ):

        report = st.session_state.get(
            "interview_report",
            {},
        )

        if report:

            st.success(
                "✅ Interview Preparation Ready!"
            )

            st.divider()

            # =================================================
            # Overview
            # =================================================

            st.subheader(
                "🎯 Interview Overview"
            )

            col1, col2 = st.columns(2)

            with col1:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        "### 💼 Target Role"
                    )

                    st.markdown(
                        f"## {report.get('job_role', 'Unknown')}"
                    )

            with col2:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        "### 🔥 Difficulty"
                    )

                    st.markdown(
                        f"## {report.get('difficulty', 'Unknown')}"
                    )

            st.divider()

            # =================================================
            # Technical Questions
            # =================================================

            st.subheader(
                "🧠 Technical Questions"
            )

            technical_questions = report.get(
                "technical_questions",
                [],
            )

            for index, item in enumerate(
                technical_questions,
                start=1,
            ):

                question = item.get(
                    "question",
                    "Question unavailable.",
                )

                answer = item.get(
                    "answer",
                    "Suggested answer unavailable.",
                )

                with st.expander(
                    f"🧠 {index}. {question}"
                ):

                    st.markdown(
                        "**Suggested Answer**"
                    )

                    st.write(
                        answer
                    )

            st.divider()

            # =================================================
            # HR Questions
            # =================================================

            st.subheader(
                "💼 HR Questions"
            )

            hr_questions = report.get(
                "hr_questions",
                [],
            )

            for index, item in enumerate(
                hr_questions,
                start=1,
            ):

                question = item.get(
                    "question",
                    "Question unavailable.",
                )

                answer = item.get(
                    "answer",
                    "Suggested answer unavailable.",
                )

                with st.expander(
                    f"💼 {index}. {question}"
                ):

                    st.markdown(
                        "**Suggested Answer**"
                    )

                    st.write(
                        answer
                    )

            st.divider()

            # =================================================
            # Behavioral Questions
            # =================================================

            st.subheader(
                "⭐ Behavioral Questions"
            )

            behavioral_questions = report.get(
                "behavioral_questions",
                [],
            )

            for index, item in enumerate(
                behavioral_questions,
                start=1,
            ):

                question = item.get(
                    "question",
                    "Question unavailable.",
                )

                answer = item.get(
                    "answer",
                    "Suggested answer unavailable.",
                )

                with st.expander(
                    f"⭐ {index}. {question}"
                ):

                    st.markdown(
                        "**Suggested Answer**"
                    )

                    st.write(
                        answer
                    )

            st.divider()

            # =================================================
            # Interview Tips
            # =================================================

            st.subheader(
                "💡 Interview Preparation Tips"
            )

            tips = report.get(
                "tips",
                [],
            )

            if tips:

                for index, tip in enumerate(
                    tips,
                    start=1,
                ):

                    st.info(
                        f"**{index}.** {tip}"
                    )

            else:

                st.info(
                    "No preparation tips available."
                )

            st.divider()

            # =================================================
            # Generate Again
            # =================================================

            if st.button(
                "🔄 Prepare for Another Interview",
                use_container_width=True,
            ):

                st.session_state.pop(
                    "interview_report",
                    None,
                )

                st.session_state.pop(
                    "interview_complete",
                    None,
                )

                st.rerun()