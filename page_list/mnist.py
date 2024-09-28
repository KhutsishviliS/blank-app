# import streamlit as st
# language = st.session_state.get('language', 'Georgian')

# if language =="Georgian":
#     st.markdown('<h1 style="color:#3A485F;">Ooops ⚙️</h1>', unsafe_allow_html=True)
#     st.markdown(""" <p style="color: #3A485F;">
#     გმადლობთ რომ დაინტერესებული ხართ ჩემი ბლოგით. ამ გვერდზე მიმდინარეობს მუშაობა და მალე მზად იქნება  
#     </p>""",unsafe_allow_html=True)
#     button_html = f"""
#     <a href="https://learndeeplearningwithsaba.streamlit.app/" target="_self">მთავარი გვერდი</button></a>
#     """
# else:
#     st.markdown('<h1 style="color:#3A485F;">Ooops ⚙️</h1>', unsafe_allow_html=True)
#     st.markdown(""" <p style="color: #3A485F;">
#     Thank you for your interest in my blog. This page is under construction and will be ready soon.
#     </p>""",unsafe_allow_html=True)
#     button_html = f"""
#     <a href="https://learndeeplearningwithsaba.streamlit.app/" target="_self">Go back</button></a>
#     """
# st.markdown(button_html, unsafe_allow_html=True)