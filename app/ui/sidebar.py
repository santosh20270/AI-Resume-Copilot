import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.

    Navigation is controlled by st.session_state.page.
    This keeps sidebar navigation and Home-page buttons synchronized.
    """

    pages = [
        "🏠 Home",
        "📄 ATS Analyzer",
        "📝 Resume Rewrite",
        "📨 Cover Letter",
        "🎤 Interview Prep",
        "📊 Skill Gap",
        "⚙️ Settings",
    ]

    # -----------------------------------------------------
    # Initialize navigation state
    # -----------------------------------------------------

    if "page" not in st.session_state:
        st.session_state.page = "🏠 Home"

    if st.session_state.page not in pages:
        st.session_state.page = "🏠 Home"

    current_page = st.session_state.page

    # Find the current page position
    current_index = pages.index(current_page)

    # -----------------------------------------------------
    # Sidebar
    # -----------------------------------------------------

    with st.sidebar:

        st.title("🚀 AI Resume Copilot")

        st.caption(
            "Your Intelligent Career Assistant"
        )

        st.divider()

        # -------------------------------------------------
        # Navigation
        # -------------------------------------------------

        selected_page = st.radio(
            "📂 Navigation",
            pages,
            index=current_index,
        )

        # -------------------------------------------------
        # Detect sidebar navigation change
        # -------------------------------------------------

        if selected_page != st.session_state.page:

            st.session_state.page = selected_page

            st.rerun()

        st.divider()

        # -------------------------------------------------
        # AI Information
        # -------------------------------------------------

        st.subheader("🤖 AI Information")

        st.success("🚀 Version 3.7")

        st.info("Gemini 3.6 Flash")

        st.divider()

        # -------------------------------------------------
        # Features
        # -------------------------------------------------

        st.subheader("✨ Features")

        st.markdown(
            """
            ✅ ATS Resume Analysis

            ✅ Resume Rewrite

            ✅ Cover Letter Generator

            ✅ Interview Preparation

            ✅ Skill Gap Analysis
            """
        )

        st.divider()

        # -------------------------------------------------
        # Footer
        # -------------------------------------------------

        st.caption(
            "Built with ❤️ using"
        )

        st.caption(
            "Python • Streamlit • Plotly • Gemini AI"
        )

    return st.session_state.page