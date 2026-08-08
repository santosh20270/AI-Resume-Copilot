import streamlit as st


def load_styles():
    """
    Premium Glassmorphism UI
    """

    st.markdown(
        """
<style>

/* ===========================================================
   GOOGLE FONT
=========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html,
body,
[class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* ===========================================================
   APP BACKGROUND
=========================================================== */

.stApp{

    background:
        linear-gradient(
            135deg,
            #0f172a 0%,
            #1e293b 35%,
            #312e81 70%,
            #4c1d95 100%
        );

    background-attachment: fixed;

}

/* ===========================================================
   MAIN CONTENT
=========================================================== */

.block-container{

    padding-top:2rem;
    padding-bottom:2rem;

}

/* ===========================================================
   SIDEBAR
=========================================================== */

[data-testid="stSidebar"]{

    background:rgba(255,255,255,0.08);

    backdrop-filter:blur(18px);

    border-right:1px solid rgba(255,255,255,0.15);

}

/* ===========================================================
   BUTTON
=========================================================== */

.stButton > button{

    width:100%;

    border-radius:14px;

    border:none;

    padding:0.8rem;

    font-weight:700;

    color:white;

    background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    transition:0.3s;

}

.stButton > button:hover{

    transform:translateY(-3px);

    box-shadow:0 12px 30px rgba(37,99,235,.45);

}

/* ===========================================================
   METRICS
=========================================================== */

[data-testid="metric-container"]{

    background:rgba(255,255,255,.08);

    border:1px solid rgba(255,255,255,.15);

    backdrop-filter:blur(18px);

    border-radius:18px;

    padding:20px;

}

/* ===========================================================
   INPUTS
=========================================================== */

.stTextInput,
.stTextArea,
.stSelectbox{

    border-radius:14px;

}

/* ===========================================================
   FILE UPLOADER
=========================================================== */

[data-testid="stFileUploader"]{

    background:rgba(255,255,255,.06);

    border:2px dashed rgba(255,255,255,.25);

    border-radius:18px;

    padding:20px;

}

/* ===========================================================
   ALERTS
=========================================================== */

.stAlert{

    border-radius:15px;

}

/* ===========================================================
   TABLES
=========================================================== */

table{

    border-radius:15px;

}

/* ===========================================================
   HEADINGS
=========================================================== */

h1{

    font-weight:800;

    letter-spacing:.5px;

}

h2{

    font-weight:700;

}

h3{

    font-weight:600;

}

/* ===========================================================
   HORIZONTAL LINE
=========================================================== */

hr{

    border:0;

    height:1px;

    background:rgba(255,255,255,.15);

}

</style>
        """,
        unsafe_allow_html=True,
    )