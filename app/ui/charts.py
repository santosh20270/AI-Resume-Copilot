import pandas as pd
import plotly.express as px
import streamlit as st


def render_skill_gap_charts(report):
    """
    Render interactive Plotly charts for the Skill Gap Dashboard.
    """

    matched = len(report["matched_skills"])
    missing = len(report["missing_skills"])

    st.divider()
    st.subheader("📊 Interactive Skill Analytics")

    col1, col2 = st.columns(2)

    # =====================================================
    # Donut Chart
    # =====================================================

    with col1:

        donut_df = pd.DataFrame(
            {
                "Category": [
                    "Matched Skills",
                    "Missing Skills",
                ],
                "Count": [
                    matched,
                    missing,
                ],
            }
        )

        donut = px.pie(
            donut_df,
            names="Category",
            values="Count",
            hole=0.55,
            title="Skill Match Distribution",
        )

        donut.update_traces(textposition="inside")

        st.plotly_chart(
            donut,
            use_container_width=True,
        )

    # =====================================================
    # Bar Chart
    # =====================================================

    with col2:

        bar_df = pd.DataFrame(
            {
                "Category": [
                    "Matched",
                    "Missing",
                ],
                "Count": [
                    matched,
                    missing,
                ],
            }
        )

        bar = px.bar(
            bar_df,
            x="Category",
            y="Count",
            title="Skill Comparison",
            text="Count",
        )

        bar.update_traces(textposition="outside")

        st.plotly_chart(
            bar,
            use_container_width=True,
        )