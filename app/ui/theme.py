import streamlit as st

from app.ui.styles import load_styles


def load_theme():
    """
    Load the application theme.
    """

    load_styles()

    st.markdown(
        """
        <style>

        /* Remove Streamlit default padding */
        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
        }

        /* Better scrollbar */

        ::-webkit-scrollbar{
            width:10px;
        }

        ::-webkit-scrollbar-thumb{
            background:#6366f1;
            border-radius:20px;
        }

        ::-webkit-scrollbar-track{
            background:transparent;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )