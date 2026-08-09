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
        # Generate Cover Letter
        # -------------------------------------------------

        try:

            with st.spinner(
                "🤖 AI is writing your cover letter..."
            ):

                cover_letter = generate_cover_letter(
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
                "your cover letter. Please try again."
            )

            st.stop()

        # -------------------------------------------------
        # Store Result
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

                try:

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

                except Exception:

                    st.error(
                        "⚠️ Word document generation failed."
                    )

            # -------------------------------------------------
            # PDF
            # -------------------------------------------------

            with col3:

                try:

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

                except Exception:

                    st.error(
                        "⚠️ PDF generation failed."
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
