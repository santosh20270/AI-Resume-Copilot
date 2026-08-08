import streamlit as st

from app.ui.ats_charts import render_ats_charts
from app.ui.ats_score_card import render_ats_score_card
from app.ui.ats_kpi_cards import render_ats_kpi_cards
from app.ui.skill_match_cards import render_skill_match_cards
from app.ui.ai_insights import render_ai_insights


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
    # Skills Analysis
    # =====================================================

    render_skill_match_cards(
        report
    )

    st.divider()

    # =====================================================
    # AI Insights
    # =====================================================

    render_ai_insights(
        report
    )