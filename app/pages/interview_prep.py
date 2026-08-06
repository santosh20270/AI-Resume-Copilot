import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.interview import generate_interview_questions


def render_interview_prep():

    st.title("🎤 AI Interview Preparation")

    st.write(
        "Upload your resume and a job description to generate "
        "AI-powered interview questions and suggested answers."
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
            key="interview_resume",
        )

    with col2:

        jd_file = st.file_uploader(
            "💼 Upload Job Description",
            type=["pdf", "docx", "txt"],
            key="interview_jd",
        )

    st.divider()

    # =====================================================
    # Generate Interview Questions
    # =====================================================

    if st.button(
        "🚀 Generate Interview Questions",
        use_container_width=True,
    ):

        if resume_file is None:
            st.error("Please upload a resume.")
            st.stop()

        if jd_file is None:
            st.error("Please upload a job description.")
            st.stop()

        os.makedirs("uploads", exist_ok=True)

        resume_path = os.path.join(
            "uploads",
            resume_file.name,
        )

        jd_path = os.path.join(
            "uploads",
            jd_file.name,
        )

        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())

        with open(jd_path, "wb") as f:
            f.write(jd_file.getbuffer())

        with st.spinner("📄 Reading Resume..."):
            resume_text = extract_text(resume_path)

        with st.spinner("💼 Reading Job Description..."):
            jd_text = extract_text(jd_path)

        with st.spinner("🤖 Generating Interview Preparation..."):
            report = generate_interview_questions(
                resume_text,
                jd_text,
            )

        st.success("✅ Interview Preparation Ready!")

        st.divider()

        st.subheader("💼 Target Job Role")
        st.info(report["job_role"])

        st.subheader("⭐ Difficulty")
        st.info(report["difficulty"])

        st.divider()

        # =====================================================
        # Technical Questions
        # =====================================================

        st.header("💻 Technical Questions")

        for index, item in enumerate(
            report["technical_questions"],
            start=1,
        ):

            with st.expander(f"Question {index}"):

                st.markdown(
                    f"**Question:** {item['question']}"
                )

                st.markdown(
                    f"**Suggested Answer:** {item['answer']}"
                )

        st.divider()

        # =====================================================
        # HR Questions
        # =====================================================

        st.header("👔 HR Questions")

        for index, item in enumerate(
            report["hr_questions"],
            start=1,
        ):

            with st.expander(f"Question {index}"):

                st.markdown(
                    f"**Question:** {item['question']}"
                )

                st.markdown(
                    f"**Suggested Answer:** {item['answer']}"
                )        
                st.divider()

        # =====================================================
        # Behavioral Questions
        # =====================================================

        st.header("🧠 Behavioral Questions")

        for index, item in enumerate(
            report["behavioral_questions"],
            start=1,
        ):

            with st.expander(f"Question {index}"):

                st.markdown(
                    f"**Question:** {item['question']}"
                )

                st.markdown(
                    f"**Suggested Answer:** {item['answer']}"
                )

        st.divider()

        # =====================================================
        # Interview Tips
        # =====================================================

        st.header("💡 Interview Tips")

        for tip in report["tips"]:
            st.success(tip)

        st.divider()

        # =====================================================
        # Save Report in Session
        # =====================================================

        st.session_state["interview_report"] = report

# =====================================================
# Download Section
# =====================================================

if "interview_report" in st.session_state:

    from app.utils.interview_docx import generate_interview_docx

    report = st.session_state["interview_report"]

    st.header("📥 Download Interview Guide")

    docx_file = generate_interview_docx(report)

    st.download_button(
        label="📝 Download Interview Guide (.docx)",
        data=docx_file,
        file_name="Interview_Preparation_Guide.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        use_container_width=True,
    )

    st.info(
        "💡 Practice these questions aloud before your interview. "
        "Customize the suggested answers with your own experiences."
    )