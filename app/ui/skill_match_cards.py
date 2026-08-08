import streamlit as st


def render_skill_match_cards(report):
    """
    Render matched and missing skills as premium skill cards.
    """

    matched_skills = report.get(
        "matched_skills",
        [],
    )

    missing_skills = report.get(
        "missing_skills",
        [],
    )

    # =====================================================
    # Section Header
    # =====================================================

    st.subheader("🧠 Skills Analysis")

    # =====================================================
    # Two-column layout
    # =====================================================

    col1, col2 = st.columns(2)

    # =====================================================
    # Matched Skills
    # =====================================================

    with col1:

        with st.container(border=True):

            st.markdown("### ✅ Matched Skills")

            if matched_skills:

                for skill in matched_skills:

                    st.success(
                        f"✓ {skill}"
                    )

            else:

                st.info(
                    "No matched skills identified."
                )

    # =====================================================
    # Missing Skills
    # =====================================================

    with col2:

        with st.container(border=True):

            st.markdown("### ❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:

                    st.warning(
                        f"＋ {skill}"
                    )

            else:

                st.success(
                    "No missing skills identified."
                )