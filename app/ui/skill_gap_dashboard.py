import streamlit as st

from app.ui.progress_cards import render_progress_cards
from app.ui.charts import render_skill_gap_charts


def render_skill_gap_dashboard(report):
    """
    Render the complete Skill Gap Dashboard.
    """

    # =====================================================
    # Dashboard Header
    # =====================================================

    st.divider()

    st.header("📊 Skill Gap Dashboard")

    st.caption(
        "Understand your current strengths, identify priority skill gaps, "
        "and follow a practical roadmap toward your target role."
    )

    # =====================================================
    # Progress Summary
    # =====================================================

    render_progress_cards(report)

    st.divider()

    # =====================================================
    # Charts
    # =====================================================

    render_skill_gap_charts(report)

    st.divider()

    # =====================================================
    # Readiness Overview
    # =====================================================

    st.subheader("🎯 Readiness Overview")

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.markdown("### 🎯 Overall Readiness")

            st.markdown(
                f"## {report.get('overall_readiness', 'Unknown')}"
            )

    with col2:

        with st.container(border=True):

            st.markdown("### ✅ Matched Skills")

            st.markdown(
                f"## {len(report.get('matched_skills', []))}"
            )

            st.caption(
                "Skills supported by your resume."
            )

    with col3:

        with st.container(border=True):

            st.markdown("### ⚠️ Missing Skills")

            st.markdown(
                f"## {len(report.get('missing_skills', []))}"
            )

            st.caption(
                "Important skills not clearly supported by your resume."
            )

    st.divider()

    # =====================================================
    # Matched Skills
    # =====================================================

    st.subheader("✅ Matched Skills")

    matched_skills = report.get(
        "matched_skills",
        [],
    )

    if matched_skills:

        columns = st.columns(3)

        for index, skill in enumerate(
            matched_skills
        ):

            with columns[index % 3]:

                st.success(
                    f"✓ {skill}"
                )

    else:

        st.info(
            "No matched skills were identified."
        )

    st.divider()

    # =====================================================
    # Missing Skills
    # =====================================================

    st.subheader("⚠️ Priority Skill Gaps")

    missing_skills = report.get(
        "missing_skills",
        [],
    )

    if missing_skills:

        columns = st.columns(3)

        for index, skill in enumerate(
            missing_skills
        ):

            with columns[index % 3]:

                st.warning(
                    f"⚠ {skill}"
                )

    else:

        st.success(
            "🎉 No major skill gaps identified."
        )

    st.divider()

    # =====================================================
    # Learning Roadmap
    # =====================================================

    st.subheader(
        "🗺️ Personalized Learning Roadmap"
    )

    st.caption(
        "Follow these steps in order, starting with the highest-priority gaps."
    )

    roadmap = report.get(
        "learning_roadmap",
        [],
    )

    if roadmap:

        for index, step in enumerate(
            roadmap,
            start=1,
        ):

            with st.container(
                border=True
            ):

                col1, col2 = st.columns(
                    [1, 8]
                )

                with col1:

                    st.markdown(
                        f"### {index}"
                    )

                with col2:

                    st.markdown(
                        f"**Step {index}**"
                    )

                    st.write(
                        step
                    )

    else:

        st.info(
            "No learning roadmap available."
        )

    st.divider()

    # =====================================================
    # Recommended Projects
    # =====================================================

    st.subheader(
        "🚀 Recommended Portfolio Projects"
    )

    st.caption(
        "Build these projects to demonstrate the missing skills in your portfolio."
    )

    projects = report.get(
        "recommended_projects",
        [],
    )

    if projects:

        columns = st.columns(2)

        for index, project in enumerate(
            projects
        ):

            with columns[index % 2]:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        f"### 🚀 Project {index + 1}"
                    )

                    st.write(
                        project
                    )

    else:

        st.info(
            "No project recommendations available."
        )

    st.divider()

    # =====================================================
    # Certifications
    # =====================================================

    st.subheader(
        "🎓 Recommended Certifications"
    )

    st.caption(
        "Certifications that may help strengthen your profile for the target role."
    )

    certifications = report.get(
        "recommended_certifications",
        [],
    )

    if certifications:

        columns = st.columns(2)

        for index, certification in enumerate(
            certifications
        ):

            with columns[index % 2]:

                with st.container(
                    border=True
                ):

                    st.markdown(
                        f"### 🎓 Certification {index + 1}"
                    )

                    st.write(
                        certification
                    )

    else:

        st.info(
            "No certification recommendations available."
        )

    st.divider()

    # =====================================================
    # Learning Time
    # =====================================================

    st.subheader(
        "⏱️ Estimated Learning Time"
    )

    with st.container(
        border=True
    ):

        st.markdown(
            "### 🗓️ Recommended Timeline"
        )

        st.markdown(
            f"## {report.get('estimated_learning_time', 'Unknown')}"
        )

        st.caption(
            "Estimated time depends on your current knowledge, "
            "study consistency, and practical experience."
        )