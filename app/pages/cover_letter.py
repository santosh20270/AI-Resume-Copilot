import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.cover_letter import generate_cover_letter
from app.utils.cover_docx import generate_cover_docx
from app.utils.cover_pdf_generator import generate_cover_pdf


def render_cover_letter():
    """
    Render the AI Cover Letter Generator page.
    """

    # =====================================================
    # Page Header
    # =====================================================

    st.title("📨 AI Cover Letter Generator")

    st.write(
        "Create a professional, truthful cover letter "
        "tailored to your resume and target job."
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
                key="cover_resume",
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
                key="cover_jd",
            )

            if jd_file:

                st.success(
                    f"✓ {jd_file.name}"
                )

    st.divider()

    # =====================================================
    # Generate Cover Letter
    # =====================================================

    if st.button(
        "📨 Generate Cover Letter",
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

        with open(
            resume_path,
            "wb",
        ) as f:

            f.write(
                resume_file.getbuffer()
            )

        # -------------------------------------------------
        # Save Job Description
        # -------------------------------------------------

        with open(
            jd_path,
            "wb",
        ) as f:

            f.write(
                jd_file.getbuffer()
            )

        # -------------------------------------------------
        # Extract Resume
        # -------------------------------------------------

        with st.spinner(
            "📄 Reading your resume..."
        ):

            resume_text = extract_text(
                resume_path
            )

        # -------------------------------------------------
        # Extract Job Description
        # -------------------------------------------------

        with st.spinner(
            "💼 Reading the job description..."
        ):

            jd_text = extract_text(
                jd_path
            )

        # -------------------------------------------------
        # Generate Cover Letter
        # -------------------------------------------------

        with st.spinner(
            "🤖 AI is writing your cover letter..."
        ):

            cover_letter = generate_cover_letter(
                resume_text,
                jd_text,
            )

        # -------------------------------------------------
        # Store result
        # -------------------------------------------------

        st.session_state[
            "cover_letter"
        ] = cover_letter

        st.session_state[
            "cover_letter_complete"
        ] = True

        st.rerun()

    # =====================================================
    # Cover Letter Result
    # =====================================================

    if st.session_state.get(
        "cover_letter_complete",
        False,
    ):

        cover_letter = st.session_state.get(
            "cover_letter",
            "",
        )

        if cover_letter:

            st.success(
                "✅ Cover Letter Generated Successfully!"
            )

            st.divider()

            # =================================================
            # Preview
            # =================================================

            st.subheader(
                "📄 Cover Letter Preview"
            )

            st.caption(
                "Review your cover letter before downloading."
            )

            with st.container(
                border=True
            ):

                st.markdown(
                    cover_letter
                )

            st.divider()

            # =================================================
            # Downloads
            # =================================================

            st.subheader(
                "📥 Download Cover Letter"
            )

            st.caption(
                "Choose your preferred format."
            )

            col1, col2, col3 = st.columns(3)

            # -------------------------------------------------
            # Markdown
            # -------------------------------------------------

            with col1:

                st.download_button(
                    label="📄 Markdown",
                    data=cover_letter,
                    file_name="Cover_Letter.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

            # -------------------------------------------------
            # DOCX
            # -------------------------------------------------

            with col2:

                docx_file = generate_cover_docx(
                    cover_letter
                )

                st.download_button(
                    label="📝 Word",
                    data=docx_file,
                    file_name="Cover_Letter.docx",
                    mime=(
                        "application/vnd.openxmlformats-officedocument."
                        "wordprocessingml.document"
                    ),
                    use_container_width=True,
                )

            # -------------------------------------------------
            # PDF
            # -------------------------------------------------

            with col3:

                pdf_file = generate_cover_pdf(
                    cover_letter
                )

                st.download_button(
                    label="📕 PDF",
                    data=pdf_file,
                    file_name="Cover_Letter.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

            st.divider()

            # =================================================
            # Generate Another
            # =================================================

            if st.button(
                "🔄 Generate Another Cover Letter",
                use_container_width=True,
            ):

                st.session_state.pop(
                    "cover_letter",
                    None,
                )

                st.session_state.pop(
                    "cover_letter_complete",
                    None,
                )

                st.rerun()
