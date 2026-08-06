import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.resume_rewriter import rewrite_resume
from app.utils.docx_generator import generate_docx


def render_resume_rewrite():

    st.title("📝 AI Resume Rewrite")

    st.write(
        "Upload your resume and a job description. "
        "AI will rewrite your resume to improve ATS compatibility."
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
            key="rewrite_resume",
        )

    with col2:

        jd_file = st.file_uploader(
            "💼 Upload Job Description",
            type=["pdf", "docx", "txt"],
            key="rewrite_jd",
        )

    st.divider()

    # =====================================================
    # Rewrite Resume
    # =====================================================

    if st.button(
        "✨ Rewrite Resume",
        use_container_width=True,
    ):

        if resume_file is None:
            st.error("Please upload a resume.")
            st.stop()

        if jd_file is None:
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

        jd_path = os.path.join(
            "uploads",
            jd_file.name,
        )

        with open(
            resume_path,
            "wb",
        ) as f:

            f.write(
                resume_file.getbuffer()
            )

        with open(
            jd_path,
            "wb",
        ) as f:

            f.write(
                jd_file.getbuffer()
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

            jd_text = extract_text(
                jd_path
            )

        with st.spinner(
            "🤖 AI is rewriting your resume..."
        ):

            rewritten = rewrite_resume(
                resume_text,
                jd_text,
            )

        st.success(
            "✅ Resume rewritten successfully!"
        )

        st.divider()

        st.markdown(rewritten)

        st.divider()

        st.subheader("📥 Download Resume")

        # =====================================================
        # Markdown Download
        # =====================================================

        st.download_button(
            label="📄 Download as Markdown (.md)",
            data=rewritten,
            file_name="Rewritten_Resume.md",
            mime="text/markdown",
            use_container_width=True,
        )

        # =====================================================
        # DOCX Download
        # =====================================================

        docx_file = generate_docx(rewritten)

        st.download_button(
            label="📝 Download as Word (.docx)",
            data=docx_file,
            file_name="Rewritten_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )