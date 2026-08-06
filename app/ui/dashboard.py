import streamlit as st


def render_dashboard(report):
    """
    Render ATS Analysis Dashboard.
    """

    st.success("✅ Resume Analysis Completed!")

    st.divider()

    # =====================================================
    # Scores
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🎯 ATS Score", f'{report["ats_score"]}%')

    with col2:
        st.metric("🔍 Keyword Match", f'{report["keyword_match"]}%')

    with col3:
        st.metric("🧠 Skills Match", f'{report["skills_match"]}%')

    with col4:
        st.metric("💼 Experience", f'{report["experience_match"]}%')

    st.progress(report["ats_score"] / 100)

    st.divider()

    # =====================================================
    # Job Role
    # =====================================================

    st.subheader("💼 Target Job Role")

    st.info(report["job_role"])

    st.divider()

    # =====================================================
    # Overall Match
    # =====================================================

    st.subheader("📊 Overall Match")

    st.success(report["overall_match"])

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
    # Strengths
    # =====================================================

    st.subheader("💪 Strengths")

    for strength in report["strengths"]:
        st.success(strength)

    st.divider()

    # =====================================================
    # Weaknesses
    # =====================================================

    st.subheader("⚠️ Weaknesses")

    for weakness in report["weaknesses"]:
        st.warning(weakness)

    st.divider()

    # =====================================================
    # Suggestions
    # =====================================================

    st.subheader("💡 Suggestions")

    for suggestion in report["suggestions"]:
        st.write(f"• {suggestion}")

    st.divider()

    # =====================================================
    # Education
    # =====================================================

    st.metric(
        "🎓 Education Match",
        f'{report["education_match"]}%'
    )

    st.divider()

    # =====================================================
    # Interview Probability
    # =====================================================

    st.subheader("🎤 Interview Probability")

    st.info(report["interview_probability"])

    st.divider()

    # =====================================================
    # Final Verdict
    # =====================================================

    st.subheader("🏁 Final Verdict")

    st.success(report["verdict"])