import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.title("📄 AI Resume Copilot")

        st.caption("Professional Resume Analysis")

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "📄 ATS Analyzer",
                "📝 Resume Rewrite",
                "📨 Cover Letter",
                "🎤 Interview Prep",
                "📊 Skill Gap",
                "⚙️ Settings",
            ],
        )

        st.divider()

        st.success("🚀 Version 3.2")

        st.info("🤖 AI Model: Gemini 3.6 Flash")

        st.caption("Built with ❤️ using Streamlit + Gemini AI")

        return page