import streamlit as st

from app.ui.ats_charts import render_ats_charts
from app.ui.ats_score_card import render_ats_score_card
from app.ui.ats_kpi_cards import render_ats_kpi_cards


def render_dashboard(report):
    """
    Render the ATS Analysis Dashboard.
    """

    # =====================================================
    # Header
    # =====================================================

    st.success("✅ Resume Analysis Completed!")

    st.divider()

    st.subheader("🎯 ATS Analysis Overview")

    # =====================================================
    # Premium ATS Score
    # =====================================================

    ats_score = int(
        report.get(
            "ats_score",
            0,
        )
    )

    render_ats_score_card(
        ats_score
    )

    # =====================================================
    # Premium KPI Cards
    # =====================================================

    render_ats_kpi_cards(
        report
    )

    st.divider()

    # =====================================================
    # Job Role
    # =====================================================

    st.subheader("💼 Target Job Role")

    st.info(
        report.get(
            "job_role",
            "Unknown",
        )
    )

    # =====================================================
    # Overall Match
    # =====================================================

    st.subheader("📊 Overall Match")

    st.success(
        report.get(
            "overall_match",
            "Unavailable",
        )
    )

    st.divider()

    # =====================================================
    # Interactive ATS Charts
    # =====================================================

    render_ats_charts(
        report
    )

    st.divider()

    # =====================================================
    # Skills
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        matched_skills = report.get(
            "matched_skills",
            [],
        )

        if matched_skills:

            for skill in matched_skills:

                st.success(
                    skill
                )

        else:

            st.info(
                "No matched skills available."
            )

    with col2:

        st.subheader("❌ Missing Skills")

        missing_skills = report.get(
            "missing_skills",
            [],
        )

        if missing_skills:

            for skill in missing_skills:

                st.error(
                    skill
                )

        else:

            st.success(
                "No missing skills identified."
            )

    st.divider()

    # =====================================================
    # Strengths
    # =====================================================

    st.subheader("💪 Strengths")

    strengths = report.get(
        "strengths",
        [],
    )

    if strengths:

        for strength in strengths:

            st.success(
                strength
            )

    else:

        st.info(
            "No strengths available."
        )

    st.divider()

    # =====================================================
    # Weaknesses
    # =====================================================

    st.subheader("⚠️ Weaknesses")

    weaknesses = report.get(
        "weaknesses",
        [],
    )

    if weaknesses:

        for weakness in weaknesses:

            st.warning(
                weakness
            )

    else:

        st.info(
            "No weaknesses available."
        )

    st.divider()

    # =====================================================
    # AI Recommendations
    # =====================================================

    st.subheader("💡 AI Recommendations")

    suggestions = report.get(
        "suggestions",
        [],
    )

    if suggestions:

        for suggestion in suggestions:

            st.write(
                f"• {suggestion}"
            )

    else:

        st.info(
            "No recommendations available."
        )

    st.divider()

    # =====================================================
    # Interview Probability
    # =====================================================

    st.subheader("🎤 Interview Probability")

    st.info(
        report.get(
            "interview_probability",
            "Unavailable",
        )
    )

    # =====================================================
    # Final Verdict
    # =====================================================

    st.subheader("🏁 Final Verdict")

    st.success(
        report.get(
            "verdict",
            "Unavailable",
        )
    )