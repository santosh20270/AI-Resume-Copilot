import streamlit as st

from app.ui.cards import metric_card
from app.ui.charts import ats_gauge
from app.ui.radar_chart import radar_chart
from app.utils.pdf_generator import generate_pdf


def render_dashboard(report: dict):

    # =========================================================
    # SUCCESS MESSAGE
    # =========================================================

    st.success("✅ Resume Analysis Completed Successfully!")

    # =========================================================
    # ATS SCORE GAUGE
    # =========================================================

    ats_gauge(report["ats_score"])

    st.divider()

    # =========================================================
    # RADAR CHART
    # =========================================================

    radar_chart(report)

    st.divider()

    # =========================================================
    # TOP KPI CARDS
    # =========================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "Job Role",
            report["job_role"],
            "💼",
            "#2563eb"
        )

    with col2:
        metric_card(
            "Interview Chance",
            report["interview_probability"],
            "🎤",
            "#9333ea"
        )

    with col3:
        metric_card(
            "Overall Match",
            report["overall_match"],
            "📊",
            "#ea580c"
        )

    st.divider()

    # =========================================================
    # MATCH ANALYSIS
    # =========================================================

    st.subheader("📊 Match Analysis")

    metrics = [
        ("Keyword Match", report["keyword_match"]),
        ("Skills Match", report["skills_match"]),
        ("Experience Match", report["experience_match"]),
        ("Education Match", report["education_match"]),
    ]

    for title, value in metrics:

        st.write(f"**{title}**")

        st.progress(value / 100)

        st.caption(f"{value}%")

    st.divider()

    # =========================================================
    # SKILLS
    # =========================================================

    left, right = st.columns(2)

    with left:

        st.subheader("✅ Matched Skills")

        if report["matched_skills"]:

            for skill in report["matched_skills"]:
                st.success(skill)

        else:
            st.info("No matching skills found.")

    with right:

        st.subheader("❌ Missing Skills")

        if report["missing_skills"]:

            for skill in report["missing_skills"]:
                st.error(skill)

        else:
            st.success("No missing skills.")

    st.divider()

    # =========================================================
    # STRENGTHS
    # =========================================================

    st.subheader("💪 Strengths")

    for item in report["strengths"]:
        st.info(item)

    st.divider()

    # =========================================================
    # WEAKNESSES
    # =========================================================

    st.subheader("⚠️ Weaknesses")

    for item in report["weaknesses"]:
        st.warning(item)

    st.divider()

    # =========================================================
    # ATS IMPROVEMENT SUGGESTIONS
    # =========================================================

    st.subheader("💡 ATS Improvement Suggestions")

    for i, suggestion in enumerate(report["suggestions"], start=1):
        st.markdown(f"**{i}.** {suggestion}")

    st.divider()

    # =========================================================
    # DOWNLOAD PDF
    # =========================================================

    st.subheader("📥 Download ATS Report")

    pdf = generate_pdf(report)

    st.download_button(
        label="📄 Download ATS Report (PDF)",
        data=pdf,
        file_name="ATS_Report.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

    st.divider()

    # =========================================================
    # RECRUITER VERDICT
    # =========================================================

    st.subheader("🏁 Recruiter Verdict")

    verdict = report["verdict"]

    if "hire" in verdict.lower():
        st.success(verdict)

    elif "shortlist" in verdict.lower():
        st.success(verdict)

    elif "maybe" in verdict.lower():
        st.warning(verdict)

    elif "reject" in verdict.lower():
        st.error(verdict)

    else:
        st.info(verdict)