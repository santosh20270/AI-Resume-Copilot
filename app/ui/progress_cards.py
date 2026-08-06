import streamlit as st


def render_progress_cards(report):
    """
    Render professional progress cards for the Skill Gap Dashboard.
    """

    st.subheader("📈 Skill Gap Summary")

    matched = len(report["matched_skills"])
    missing = len(report["missing_skills"])

    total = matched + missing

    if total == 0:
        percentage = 0
    else:
        percentage = int((matched / total) * 100)

    st.metric(
        "🎯 Skill Match",
        f"{percentage}%"
    )

    st.progress(percentage / 100)

    st.caption(f"{matched} matched skills • {missing} missing skills")

    st.divider()