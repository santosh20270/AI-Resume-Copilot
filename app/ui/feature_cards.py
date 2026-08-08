import streamlit as st


def render_feature_cards():
    """
    Render clickable premium feature cards.
    """

    cards = [
        (
            "📄",
            "ATS Analyzer",
            "Analyze your resume against a job description using AI.",
            "📄 ATS Analyzer",
        ),
        (
            "📝",
            "Resume Rewrite",
            "Improve your resume with AI-powered rewriting.",
            "📝 Resume Rewrite",
        ),
        (
            "📨",
            "Cover Letter",
            "Generate a personalized professional cover letter.",
            "📨 Cover Letter",
        ),
        (
            "🎤",
            "Interview Prep",
            "Prepare for technical and HR interviews.",
            "🎤 Interview Prep",
        ),
        (
            "📊",
            "Skill Gap",
            "Discover missing skills and build a learning roadmap.",
            "📊 Skill Gap",
        ),
        (
            "⚙️",
            "Settings",
            "View application and AI configuration information.",
            "⚙️ Settings",
        ),
    ]

    # -----------------------------------------------------
    # Card Styling
    # -----------------------------------------------------

    st.markdown(
        """
        <style>

        .native-feature-title {
            font-size: 1.25rem;
            font-weight: 700;
            margin-top: 8px;
        }

        .native-feature-description {
            color: #cbd5e1;
            font-size: 0.9rem;
            line-height: 1.5;
            min-height: 55px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # Create 2-column layout
    # -----------------------------------------------------

    for row in range(0, len(cards), 2):

        col1, col2 = st.columns(2)

        row_cards = cards[row:row + 2]

        for col, card in zip(
            (col1, col2),
            row_cards,
        ):

            icon, title, description, page = card

            with col:

                # Native Streamlit container
                with st.container(border=True):

                    st.markdown(
                        f"## {icon}"
                    )

                    st.markdown(
                        f"### {title}"
                    )

                    st.markdown(
                        f'<div class="native-feature-description">'
                        f'{description}'
                        f'</div>',
                        unsafe_allow_html=True,
                    )

                    st.write("")

                    if st.button(
                        f"Open {title} →",
                        key=f"feature_{title}",
                        use_container_width=True,
                    ):

                        st.session_state.page = page

                        st.rerun()

        st.write("")