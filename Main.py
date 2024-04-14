import pickle
from pathlib import Path
from pages import nada

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator

pages = {
    "Page 1": nada    
}

#selected_page = st.radio("Selecciona una página", list(pages.keys()))
#pages[selected_page]()

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="streamlit Dashboard", page_icon=":bar_chart:", layout="wide")

hide_bar= """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        visibility:hidden;
        width: 0px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        visibility:hidden;
    }
    </style>
"""

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller","bharath"]
usernames = ["pparker", "rmiller","bharath"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "SIPL_dashboard", "abcdef")

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("Please enter your username and password")
    st.markdown(hide_bar, unsafe_allow_html=True)


if authentication_status:
    # # ---- SIDEBAR ----
    st.sidebar.title(f"Welcome {name}")
    st.sidebar.header("Gandaberunda - AI-based Helping Hands for Police Investigation")
    st.title("We are team Gandaberunda.")
    st.write("Our Idea is to create an AI-based helping hands to ease the process of Police Investigation by providing streamline tools that can help them solve cases easily.")

    ###about ....
    # Embed the Google Slides presentation
    st.markdown(
        """
        <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQXPJoOJCqwE2Hgn2djqR5snssdzvN90HJJ1qceRCLkma0MOdG3neH2uy8Yu5hSVKFoeKl9enXXfdmb/embed?start=true&loop=true&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.success("Select a page above.")

    ###---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)


    authenticator.logout("Logout", "sidebar")
