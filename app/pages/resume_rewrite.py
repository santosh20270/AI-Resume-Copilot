import os
import streamlit as st

from app.services.document_service import extract_text
from app.ai.resume_rewriter import rewrite_resume
from app.utils.docx_generator import generate_docx
from app.utils.pdf_generator import generate_pdf


def render_resume_rewrite():
    """
    Render the AI Resume Rewrite page.
    """

    # =====================================================
    # Page Header
    # =====================================================

    st.title("📝 AI Resume Rewrite")

    st.write(
        "Optimize your resume for a target job while keeping "
        "your experience and information completely truthful."
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
                "Upload your current resume",
                type=[
                    "pdf",
                    "docx",
                    "txt",
                ],
                key="rewrite_resume",
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
                key="rewrite_jd",
            )

            if jd_file:

                st.success(
                    f"✓ {jd_file.name}"
                )

    st.divider()

    # =====================================================
    # Rewrite Button
    # =====================================================

    if st.button(
        "✨ Rewrite Resume with AI",
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
        # AI Rewrite
        # -------------------------------------------------

        with st.spinner(
            "🤖 AI is optimizing your resume..."
        ):

            rewritten = rewrite_resume(
                resume_text,
                jd_text,
            )

        # -------------------------------------------------
        # Store result
        # -------------------------------------------------

        st.session_state[
            "rewritten_resume"
        ] = rewritten

        st.session_state[
            "rewrite_complete"
        ] = True

        st.rerun()

    # =====================================================
    # Rewritten Resume
    # =====================================================

    if st.session_state.get(
        "rewrite_complete",
        False,
    ):

        rewritten = st.session_state.get(
            "rewritten_resume",
            "",
        )

        if rewritten:

            st.success(
                "✅ Resume rewritten successfully!"
            )

            st.divider()

            # =================================================
            # Preview
            # =================================================

            st.subheader(
                "✨ Optimized Resume"
            )

            st.caption(
                "Review the AI-generated resume before downloading."
            )

            with st.container(
                border=True
            ):

                st.markdown(
                    rewritten
                )

            st.divider()

            # =================================================
            # Downloads
            # =================================================

            st.subheader(
                "📥 Download Resume"
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
                    data=rewritten,
                    file_name="Rewritten_Resume.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

            # -------------------------------------------------
            # DOCX
            # -------------------------------------------------

            with col2:

                docx_file = generate_docx(
                    rewritten
                )

                st.download_button(
                    label="📝 Word",
                    data=docx_file,
                    file_name="Rewritten_Resume.docx",
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

                pdf_file = generate_pdf(
                    rewritten
                )

                st.download_button(
                    label="📕 PDF",
                    data=pdf_file,
                    file_name="Rewritten_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

            st.divider()

            # =================================================
            # Rewrite Again
            # =================================================

            if st.button(
                "🔄 Rewrite Another Resume",
                use_container_width=True,
            ):

                st.session_state.pop(
                    "rewritten_resume",
                    None,
                )

                st.session_state.pop(
                    "rewrite_complete",
                    None,
                )

                st.rerun()