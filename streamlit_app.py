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
    #img_base64 = get_img_as_base64("images/magicpattern1.png")
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
###############################################
about =st.Page(
    page="pages/about.py",
    title="About Me",
    icon="🧑"
    
)
project = st.Page(
    page="pages/projects.py",
    title="Project",
    icon="📚"
    
)

contact_page = st.Page(
    page="pages/contact.py",
    title="Contact",
    icon="✉️"
)
main_page = st.Page(
    page="streamlit_app.py",
    title="Main Page",
    icon="🤖",
    default= True
)
# ----------- NAVIGATION ----------- #
#pg = st.navigation(pages=[main_page, project,contact_page,about])
#pg.run()

# Function to display a card with image and text
def display_card(image_url, title, description, page_name, link_text):
    # Create two columns for the image and text
    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control the space distribution

    # Column 1: Display the image
    with col1:
        st.image(image_url, use_column_width=True)  # Auto-resizes image to fit the column width

    # Column 2: Display text information
    with col2:
        st.markdown(f"### {title}")  # Title in a larger font size
        st.write(description)  # Main description or information text
        if st.button(link_text, key=f"btn_{title}"):
            st.switch_page(page_name)

st.markdown("## AI Fashion MNIST Cards")  # Page title

# Example usage of the card
image_url = "images/tfcube.webp"  # Replace with your actual image URL
title = "AI Fashion MNIST"
description = "A model that classifies fashion items using AI. Explore the dataset and learn more."
page_name = "pages/projects.py"  # This should match the filename of your projects page
link_text = "Learn More"
#pname= "pages/about.py"
#ttle= "MMN"

# Call the display_card function
display_card(image_url, title, description, page_name, link_text)
#display_card(image_url, ttle, description,pname, link_text)



