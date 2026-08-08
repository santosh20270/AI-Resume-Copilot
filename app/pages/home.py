import streamlit as st

from app.ui.hero import render_hero
from app.ui.feature_cards import render_feature_cards


def render_home():
    """
    Render the Home page.
    """

    # =====================================================
    # Hero Section
    # =====================================================

    render_hero()

    # =====================================================
    # Statistics
    # =====================================================

    st.subheader("📊 Platform Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🤖 AI Modules",
            "5"
        )

    with col2:
        st.metric(
            "📄 Export Formats",
            "PDF + DOCX"
        )

    with col3:
        st.metric(
            "📈 Analytics",
            "Interactive"
        )

    st.divider()

    # =====================================================
    # Feature Cards
    # =====================================================

    st.subheader("✨ Platform Features")

    render_feature_cards()

    st.divider()

    # =====================================================
    # Technology Stack
    # =====================================================

    st.subheader("🛠 Technology Stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.info("🐍 Python")
        st.info("⚡ Streamlit")

    with tech2:
        st.info("🤖 Gemini AI")
        st.info("📊 Plotly")

    with tech3:
        st.info("📄 PyMuPDF")
        st.info("📝 python-docx")

    st.divider()

    # =====================================================
    # Quick Start
    # =====================================================

    st.subheader("🚀 Quick Start")

    st.markdown(
        """
1. 📄 Upload your Resume and Job Description.

2. 🤖 Analyze ATS compatibility.

3. 📝 Rewrite your Resume using AI.

4. 📨 Generate a Cover Letter.

5. 🎤 Prepare for Interviews.

6. 📊 Analyze your Skill Gap.
"""
    )

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.caption("© 2026 Santosh")

    st.caption(
        "Built with ❤️ using Python, Streamlit, Plotly and Google Gemini AI."
    )