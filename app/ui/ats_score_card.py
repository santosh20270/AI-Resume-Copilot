import streamlit as st


def render_ats_score_card(score):
    """
    Render a premium ATS score card using native Streamlit components.
    """

    score = int(score)
    score = max(0, min(score, 100))

    # -----------------------------------------------------
    # Rating
    # -----------------------------------------------------

    if score >= 85:
        icon = "🟢"
        rating = "Excellent Match"

    elif score >= 70:
        icon = "🔵"
        rating = "Strong Match"

    elif score >= 50:
        icon = "🟡"
        rating = "Moderate Match"

    else:
        icon = "🔴"
        rating = "Needs Improvement"

    # -----------------------------------------------------
    # Card Styling
    # -----------------------------------------------------

    st.markdown(
        """
        <style>

        div[data-testid="stVerticalBlock"] .ats-card {
            background:
                linear-gradient(
                    135deg,
                    rgba(37, 99, 235, 0.20),
                    rgba(124, 58, 237, 0.20)
                );

            border: 1px solid rgba(255,255,255,0.14);

            border-radius: 24px;

            padding: 30px;

            margin-bottom: 25px;

            box-shadow:
                0 15px 40px rgba(0,0,0,0.25);
        }

        .ats-label {
            color: #cbd5e1;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .ats-number {
            font-size: 64px;
            font-weight: 800;
            margin-top: 8px;
            color: white;
        }

        .ats-rating {
            color: #e2e8f0;
            font-size: 20px;
            font-weight: 700;
            margin-top: 5px;
        }

        .ats-description {
            color: #cbd5e1;
            font-size: 14px;
            margin-top: 8px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # Native Streamlit Card
    # -----------------------------------------------------

    with st.container(border=True):

        st.markdown(
            "🎯 Overall ATS Score"
        )

        st.markdown(
            f"# {score}%"
        )

        st.markdown(
            f"### {icon} {rating}"
        )

        st.caption(
            "Resume compatibility with the target job description"
        )

        st.progress(
            score / 100
        )