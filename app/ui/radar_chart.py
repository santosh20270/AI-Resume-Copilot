import plotly.graph_objects as go
import streamlit as st


def radar_chart(report):

    categories = [
        "Keywords",
        "Skills",
        "Experience",
        "Education"
    ]

    values = [
        report["keyword_match"],
        report["skills_match"],
        report["experience_match"],
        report["education_match"]
    ]

    # Close the polygon
    categories = categories + [categories[0]]
    values = values + [values[0]]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            fillcolor="rgba(59,130,246,0.35)",
            line=dict(
                color="#3B82F6",
                width=3
            ),
            name="Resume"
        )
    )

    fig.update_layout(

        title="📊 Resume Match Overview",

        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",

        font=dict(
            color="white"
        ),

        polar=dict(

            bgcolor="#0F172A",

            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor="#334155",
                tickfont=dict(color="white")
            ),

            angularaxis=dict(
                tickfont=dict(color="white"),
                gridcolor="#334155"
            ),
        ),

        showlegend=False,
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displaylogo": False
        }
    )