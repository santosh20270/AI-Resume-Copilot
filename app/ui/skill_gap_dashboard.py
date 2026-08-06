import streamlit as st

from app.ui.progress_cards import render_progress_cards
from app.ui.charts import render_skill_gap_charts


def render_skill_gap_dashboard(report):
    """
    Render the complete Skill Gap Dashboard.
    """

    st.divider()

    st.header("📊 Skill Gap Dashboard")

    # =====================================================
    # Progress Summary
    # =====================================================

    render_progress_cards(report)

    # =====================================================
    # Charts
    # =====================================================

    render_skill_gap_charts(report)

    # =====================================================
    # Top Metrics
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Overall Readiness",
            report["overall_readiness"],
        )

    with col2:
        st.metric(
            "✅ Matched Skills",
            len(report["matched_skills"]),
        )

    with col3:
        st.metric(
            "❌ Missing Skills",
            len(report["missing_skills"]),
        )

    st.divider()

    # =====================================================
    # Skills
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        for skill in report["matched_skills"]:
            st.success(skill)

    with col2:

        st.subheader("❌ Missing Skills")

        for skill in report["missing_skills"]:
            st.error(skill)

    st.divider()

    # =====================================================
    # Learning Roadmap
    # =====================================================

    st.subheader("🛣️ Learning Roadmap")

    for index, step in enumerate(report["learning_roadmap"], start=1):
        st.write(f"**Step {index}:** {step}")

    st.divider()

    # =====================================================
    # Recommended Projects
    # =====================================================

    st.subheader("💼 Recommended Projects")

    for project in report["recommended_projects"]:
        st.info(project)

    st.divider()

    # =====================================================
    # Certifications
    # =====================================================

    st.subheader("🎓 Recommended Certifications")

    for cert in report["recommended_certifications"]:
        st.info(cert)

    st.divider()

    # =====================================================
    # Estimated Learning Time
    # =====================================================

    st.metric(
        "⏳ Estimated Learning Time",
        report["estimated_learning_time"],
    )