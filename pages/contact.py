import streamlit as st
from streamlit_app import page_design,get_img_as_base64
get_img_as_base64()
page_design()
with st.form("contact_form"):
    name = st.text_input("First Name")
    email = st.text_input("Email Adress")
    message = st.text_area("your message")
    submit_bt = st.form_submit_button("Submit")

    if submit_bt:
        st.success("Message successfully sent!")