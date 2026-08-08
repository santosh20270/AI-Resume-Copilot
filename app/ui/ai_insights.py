import streamlit as st


def render_ai_insights(report):
    """
    Render AI-generated resume insights.
    """

    strengths = report.get(
        "strengths",
        [],
    )

    weaknesses = report.get(
        "weaknesses",
        [],
    )

    suggestions = report.get(
        "suggestions",
        [],
    )

    interview_probability = report.get(
        "interview_probability",
        "Unavailable",
    )

    verdict = report.get(
        "verdict",
        "Unavailable",
    )

    # =====================================================
    # Section Header
    # =====================================================

    st.subheader("🤖 AI Resume Insights")

    st.caption(
        "AI-powered recommendations based on your resume and target job."
    )

    # =====================================================
    # Strengths + Weaknesses
    # =====================================================

    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # Strengths
    # -----------------------------------------------------

    with col1:

        with st.container(border=True):

            st.markdown("### 💪 Resume Strengths")

            if strengths:

                for strength in strengths:

                    st.success(
                        f"✓ {strength}"
                    )

            else:

                st.info(
                    "No strengths identified."
                )

    # -----------------------------------------------------
    # Weaknesses
    # -----------------------------------------------------

    with col2:

        with st.container(border=True):

            st.markdown("### ⚠️ Areas to Improve")

            if weaknesses:

                for weakness in weaknesses:

                    st.warning(
                        f"! {weakness}"
                    )

            else:

                st.info(
                    "No major weaknesses identified."
                )

    st.write("")

    # =====================================================
    # Recommendations
    # =====================================================

    with st.container(border=True):

        st.markdown("### 💡 AI Recommendations")

        if suggestions:

            for index, suggestion in enumerate(
                suggestions,
                start=1,
            ):

                st.write(
                    f"**{index}.** {suggestion}"
                )

        else:

            st.info(
                "No recommendations available."
            )

    st.write("")

    # =====================================================
    # Interview Probability + Verdict
    # =====================================================

    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # Interview Probability
    # -----------------------------------------------------

    with col1:

        with st.container(border=True):

            st.markdown(
                "### 🎤 Interview Probability"
            )

            st.markdown(
                f"## {interview_probability}"
            )

            st.caption(
                "Estimated likelihood of progressing to an interview."
            )

    # -----------------------------------------------------
    # Final Verdict
    # -----------------------------------------------------

    with col2:

        with st.container(border=True):

            st.markdown(
                "### 🏁 Final Verdict"
            )

            st.write(
                verdict
            )