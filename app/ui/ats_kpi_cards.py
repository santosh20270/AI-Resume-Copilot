import streamlit as st


def render_ats_kpi_cards(report):
    """
    Render premium ATS KPI cards.
    """

    metrics = [
        (
            "🔍",
            "Keyword Match",
            int(report.get("keyword_match", 0)),
        ),
        (
            "🧠",
            "Skills Match",
            int(report.get("skills_match", 0)),
        ),
        (
            "💼",
            "Experience Match",
            int(report.get("experience_match", 0)),
        ),
        (
            "🎓",
            "Education Match",
            int(report.get("education_match", 0)),
        ),
    ]

    # =====================================================
    # Styling
    # =====================================================

    st.markdown(
        """
        <style>

        .kpi-title {
            font-size: 14px;
            font-weight: 600;
            color: #cbd5e1;
            margin-bottom: 8px;
        }

        .kpi-value {
            font-size: 34px;
            font-weight: 800;
            color: white;
            line-height: 1.1;
        }

        .kpi-label {
            font-size: 12px;
            color: #94a3b8;
            margin-top: 5px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # Cards
    # =====================================================

    columns = st.columns(4)

    for column, (icon, title, value) in zip(
        columns,
        metrics,
    ):

        with column:

            with st.container(border=True):

                st.markdown(
                    f"### {icon}"
                )

                st.markdown(
                    f"**{title}**"
                )

                st.markdown(
                    f"# {value}%"
                )

                st.progress(
                    max(
                        0,
                        min(value, 100),
                    ) / 100
                )

                if value >= 85:

                    st.caption(
                        "🟢 Excellent"
                    )

                elif value >= 70:

                    st.caption(
                        "🔵 Strong"
                    )

                elif value >= 50:

                    st.caption(
                        "🟡 Moderate"
                    )

                else:

                    st.caption(
                        "🔴 Needs Improvement"
                    )