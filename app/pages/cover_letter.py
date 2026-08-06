import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.cover_letter import generate_cover_letter
from app.utils.cover_docx import generate_cover_docx


def render_cover_letter():

    st.title("📨 AI Cover Letter Generator")

    st.write(
        "Generate a professional ATS-friendly cover letter "
        "tailored to any job description."
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
            key="cover_resume",
        )

    with col2:

        jd_file = st.file_uploader(
            "💼 Upload Job Description",
            type=["pdf", "docx", "txt"],
            key="cover_jd",
        )

    st.divider()

    # =====================================================
    # Generate Cover Letter
    # =====================================================

    if st.button(
        "📨 Generate Cover Letter",
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

        with st.spinner("🤖 AI is generating your cover letter..."):
            cover_letter = generate_cover_letter(
                resume_text,
                jd_text,
            )

        st.success("✅ Cover Letter Generated Successfully!")

        st.divider()

        st.subheader("📄 Preview")

        st.markdown(cover_letter)

        st.divider()

        st.subheader("📥 Download")

        # =====================================================
        # Markdown Download
        # =====================================================

        st.download_button(
            label="📄 Download as Markdown (.md)",
            data=cover_letter,
            file_name="Cover_Letter.md",
            mime="text/markdown",
            use_container_width=True,
        )

        # =====================================================
        # DOCX Download
        # =====================================================

        docx_file = generate_cover_docx(cover_letter)

        st.download_button(
            label="📝 Download as Word (.docx)",
            data=docx_file,
            file_name="Cover_Letter.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )

        st.divider()

        st.info(
            "💡 Review the generated cover letter before submitting it "
            "to ensure it matches the specific role and your personal style."
        )
