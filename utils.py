import streamlit as st


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/96tvTKc.png);
                background-repeat: no-repeat;
                padding-top: 50px;
                background-position: 20px 30px;
                background-size: 75% 40%;
                margin-top: 10%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
