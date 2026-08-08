import streamlit as st


def render_hero():

    st.markdown("""
<style>

.hero-card{
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    border-radius:25px;
    padding:40px;
    color:white;
    margin-bottom:30px;
}

.hero-title{
    font-size:48px;
    font-weight:800;
}

.hero-sub{
    font-size:22px;
    margin-top:10px;
    color:#e5e7eb;
}

.hero-desc{
    margin-top:20px;
    font-size:18px;
    line-height:1.7;
}

.badge{
    display:inline-block;
    background:rgba(255,255,255,.15);
    padding:8px 16px;
    border-radius:999px;
    margin:8px 8px 0 0;
}

</style>

<div class="hero-card">

<h1 class="hero-title">🚀 AI Resume Copilot</h1>

<div class="hero-sub">
Your Intelligent Career Assistant
</div>

<div class="hero-desc">
Analyze resumes, rewrite resumes, generate AI cover letters,
prepare for interviews, and discover your skill gaps —
all in one intelligent platform.
</div>

<br>

<span class="badge">📄 ATS Analyzer</span>
<span class="badge">📝 Resume Rewrite</span>
<span class="badge">📨 Cover Letter</span>
<span class="badge">🎤 Interview Prep</span>
<span class="badge">📊 Skill Gap</span>

</div>

""", unsafe_allow_html=True)