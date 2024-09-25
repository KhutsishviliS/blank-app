import streamlit as st

st.markdown('<h1 style="color:#3A485F;">გამარჯობა ⚙️</h1>', unsafe_allow_html=True)

st.markdown(""" <p style="color: #3A485F;">
გმადლობთ რომ დაინტერესებული ხართ ჩემი ბლოგით. ამ გვერდზე მიმდინარეობს მუშაობა და მალე მზად იქნება  
</p>""",unsafe_allow_html=True)
button_html = f"""
    <a href="https://learndeeplearningwithsaba.streamlit.app/" target="_self">მთავარი გვერდი</button></a>
    """
st.markdown(button_html, unsafe_allow_html=True)