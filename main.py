import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_app, contact, about, main

st.set_page_config(
    page_title="Deep Learning"

                    )

class MultiApp:
    def __init__(self):
        self.apps=[]
    
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Deep Learning With Saba",
                options=["Home","Projects"],
                default_index=0

            )
        
        if app == "Home":
            main.run()
        elif app == "Projects":
            streamlit_app.run()
