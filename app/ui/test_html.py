import streamlit as st

st.set_page_config(page_title="HTML Test")

st.title("HTML Test")

st.markdown(
    """
    <div style="
        background:#2563eb;
        color:white;
        padding:30px;
        border-radius:15px;
        text-align:center;
        font-size:30px;
        font-weight:bold;
    ">
        HTML IS WORKING ✅
    </div>
    """,
    unsafe_allow_html=True,
)