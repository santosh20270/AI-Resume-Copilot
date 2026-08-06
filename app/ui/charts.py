import plotly.graph_objects as go
import streamlit as st


def ats_gauge(score: int):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,

            number={
                "suffix": "/100",
                "font": {
                    "size": 48,
                    "color": "white"
                }
            },

            title={
                "text": "<b>ATS Score</b>",
                "font": {
                    "size": 28,
                    "color": "white"
                }
            },

            gauge={

                "axis": {
                    "range": [0, 100],
                    "tickcolor": "white",
                    "tickfont": {"color": "white"}
                },

                "bar": {
                    "color": "#3B82F6",
                    "thickness": 0.35
                },

                "bgcolor": "#1E293B",

                "borderwidth": 2,
                "bordercolor": "#334155",

                "steps": [
                    {
                        "range": [0, 40],
                        "color": "#EF4444"
                    },
                    {
                        "range": [40, 70],
                        "color": "#EAB308"
                    },
                    {
                        "range": [70, 100],
                        "color": "#22C55E"
                    }
                ],

                "threshold": {
                    "line": {
                        "color": "white",
                        "width": 5
                    },
                    "thickness": 0.8,
                    "value": score
                }
            }
        )
    )

    fig.update_layout(

        height=360,

        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",

        font={
            "color": "white"
        },

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displaylogo": False
        }
    )