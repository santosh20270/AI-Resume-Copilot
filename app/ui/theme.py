import streamlit as st


def load_theme():

    st.markdown(
        """
        <style>

        .stApp{
            background:#0F172A;
            color:white;
        }

        section[data-testid="stSidebar"]{
            background:#111827;
        }

        h1,h2,h3,h4,h5,h6{
            color:white !important;
        }

        p,label,span{
            color:#cbd5e1 !important;
        }

        div[data-testid="metric-container"]{
            background:#1E293B;
            border:1px solid #334155;
            border-radius:15px;
            padding:20px;
        }

        section[data-testid="stFileUploader"]{
            background:#1E293B;
            border:1px solid #334155;
            border-radius:15px;
            padding:20px;
        }

        .stButton>button{
            background:#2563EB;
            color:white;
            border:none;
            border-radius:12px;
            height:3rem;
            font-weight:bold;
        }

        .stButton>button:hover{
            background:#1D4ED8;
            color:white;
        }

        div[data-testid="stAlert"]{
            border-radius:12px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )