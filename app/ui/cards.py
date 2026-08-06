import streamlit as st


def metric_card(title, value, emoji="📊", color="#2563eb"):
    with st.container(border=True):
        st.metric(
            label=f"{emoji} {title}",
            value=str(value)
        )