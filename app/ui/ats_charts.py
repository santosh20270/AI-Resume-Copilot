import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def render_ats_charts(report):
    """
    Render interactive ATS analytics charts.
    """

    # =====================================================
    # Extract Scores
    # =====================================================

    keyword_match = int(report.get("keyword_match", 0))
    skills_match = int(report.get("skills_match", 0))
    experience_match = int(report.get("experience_match", 0))
    education_match = int(report.get("education_match", 0))

    matched_skills = report.get("matched_skills", [])
    missing_skills = report.get("missing_skills", [])

    # =====================================================
    # Score Analysis
    # =====================================================

    st.subheader("📊 Resume Match Analytics")

    score_df = pd.DataFrame(
        {
            "Category": [
                "Keywords",
                "Skills",
                "Experience",
                "Education",
            ],
            "Score": [
                keyword_match,
                skills_match,
                experience_match,
                education_match,
            ],
        }
    )

    bar_chart = px.bar(
        score_df,
        x="Category",
        y="Score",
        text="Score",
        range_y=[0, 100],
        title="Resume Match Score",
    )

    bar_chart.update_traces(
        textposition="outside"
    )

    bar_chart.update_layout(
        yaxis_title="Match %",
        xaxis_title="",
        showlegend=False,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True,
    )

    # =====================================================
    # Matched vs Missing Skills
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        skill_df = pd.DataFrame(
            {
                "Category": [
                    "Matched Skills",
                    "Missing Skills",
                ],
                "Count": [
                    len(matched_skills),
                    len(missing_skills),
                ],
            }
        )

        donut_chart = px.pie(
            skill_df,
            names="Category",
            values="Count",
            hole=0.55,
            title="Skills Distribution",
        )

        donut_chart.update_layout(
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20,
            ),
        )

        st.plotly_chart(
            donut_chart,
            use_container_width=True,
        )

    # =====================================================
    # Radar Chart
    # =====================================================

    with col2:

        categories = [
            "Keywords",
            "Skills",
            "Experience",
            "Education",
        ]

        values = [
            keyword_match,
            skills_match,
            experience_match,
            education_match,
        ]

        radar = go.Figure()

        radar.add_trace(
            go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill="toself",
                name="Resume Match",
            )
        )

        radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                )
            ),
            title="Match Profile",
            showlegend=False,
            margin=dict(
                l=30,
                r=30,
                t=60,
                b=30,
            ),
        )

        st.plotly_chart(
            radar,
            use_container_width=True,
        )