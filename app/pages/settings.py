import platform
import streamlit as st


def render_settings():
    """
    Render the Settings page.
    """

    st.title("⚙️ Settings")

    st.caption("AI Resume Copilot Configuration")

    st.divider()

    # =====================================================
    # Application Information
    # =====================================================

    st.subheader("📦 Application Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Application", "AI Resume Copilot")
        st.metric("Version", "3.3")
        st.metric("Developer", "Santosh")

    with col2:
        st.metric("AI Model", "Gemini 3.6 Flash")
        st.metric("Python", platform.python_version())
        st.metric("Framework", "Streamlit")

    st.divider()

    # =====================================================
    # Enabled Features
    # =====================================================

    st.subheader("✨ Enabled Features")

    features = [
        "📄 ATS Resume Analyzer",
        "📝 AI Resume Rewrite",
        "📨 AI Cover Letter Generator",
        "🎤 AI Interview Preparation",
        "📊 AI Skill Gap Dashboard",
    ]

    for feature in features:
        st.success(feature)

    st.divider()

    # =====================================================
    # Project Statistics
    # =====================================================

    st.subheader("📊 Project Statistics")

    stat1, stat2, stat3 = st.columns(3)

    with stat1:
        st.metric("AI Modules", "5")

    with stat2:
        st.metric("Pages", "6")

    with stat3:
        st.metric("Export Formats", "PDF + DOCX")

    st.divider()

    # =====================================================
    # System Status
    # =====================================================

    st.subheader("🟢 System Status")

    st.success("Application is running successfully.")

    st.info("All AI modules are loaded.")

    st.divider()

    # =====================================================
    # Repository
    # =====================================================

    st.subheader("🔗 Project Repository")

    st.link_button(
        "🌐 Open GitHub Repository",
        "https://github.com/santosh20270/AI-Resume-Copilot",
    )

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.caption("© 2026 Santosh")
    st.caption("Built with ❤️ using Python, Streamlit and Google Gemini AI.")