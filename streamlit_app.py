import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from streamlit_option_menu import option_menu
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set up the background image in Streamlit page design
def page_design():
    page_bg_img = f"""
    <style>
    .main {{
        background-color: #274f69;
    }}
    [data-testid="stVerticalBlock"] {{
        background-color: white;
    }}
    [data-testid="stAppViewBlockContainer"]{{
        background-color: white;
    }}
    [data-testid="stHeader"] {{
        background-color: #FE6F00;
    }}
    [data-testid="stSidebarContent"] {{
        background-color: white;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

page_design()

# Add language selection dropdown
if 'Georgian' in st.session_state:
    st.session_state['language'] = 'Georgian'  # Set default language to Georgian

language = st.selectbox("Choose Language ", ["Georgian", "English"])

# Store the selected language in session state
st.session_state['language'] = language

###############################################
about = st.Page(
    page="pages/about.py",
    title="About Me",
    icon="🧑"
)
project = st.Page(
    page="pages/projects.py",
    title="Fashion MNIST",
    icon="📚"
)
contact_page = st.Page(
    page="pages/contact.py",
    title="Contact",
    icon="✉️"
)
main_page = st.Page(
    page="pages/main.py",
    title="Main Page",
    icon="🤖",
    default=True
)
digit_mnist = st.Page(
    page="pages/mnist.py",
    title="MNIST Digit Classifier",
    icon="📚"
)

# ----------- NAVIGATION ----------- #
pg = st.navigation(pages=[main_page, project, digit_mnist, contact_page, about])
pg.run()
