import streamlit as st
from streamlit_app import page_design

page_design()
language = st.session_state.get('English', 'Georgian')

if language =="Georgian":
    # Custom color for the title
    st.markdown('<h1 style="color:#3A485F;">გამარჯობა</h1>', unsafe_allow_html=True)

    # Custom color for the paragraph and bullet points
    st.markdown('''
    <p style="color:#3A485F;">
    მე საბა ვარ, ხელოვნური ინტელექტის ენთუზიასტი და ამ ბლოგის ავტორი. 
    ჩემი მიზანია, AI, Machine Learning და Deep Learning შესახებ ცოდნა ხელმისაწვდომი გავხადო ყველასთვის.<br>
    პროფესიით ვმუშაობ მონაცემთა და პროცესების დამუშავების მიმართულებით. 
    ეს გამოცდილება მაძლევს საშუალებას ვისაუბრო AI-ის პრაქტიკულ გამოყენებაზე რეალურ სამყაროში.<br>
    ამ ბლოგის მეშვეობით, ჩემი მისიაა:
    </p>

    <ul style="color:#3A485F;">
        <li>გავამარტივო და თვალსაჩინო გავხადო რთული AI კონცეფციები</li>
        <li>წარმოვადგინო პრაქტიკული მაგალითები ტექნოლოგიების გამოყენებაზე</li>
        <li>გავაღვივო ინტერესი და ცნობისმოყვარეობა AI-ის მიმართ</li>
    </ul>
    ''', unsafe_allow_html=True)

else:
    # Custom color for the title
    st.markdown('<h1 style="color:#3A485F;">Hello</h1>', unsafe_allow_html=True)

    # Custom color for the paragraph and bullet points
    st.markdown('''
    <p style="color:#3A485F;">
    My name is Saba, an artificial intelligence enthusiast and the author of this blog. 
    My goal is to make knowledge about AI, Machine Learning, and Deep Learning accessible to everyone.<br>
    Professionally, I work in data and process engineering. 
    This experience allows me to discuss the practical applications of AI in the real world.<br>
                
    Through this blog, my mission is to:
    </p>

    <ul style="color:#3A485F;">
        <li>Simplify and visualize complex AI concepts</li>
        <li>Present practical examples of technology usage</li>
        <li>Spark interest and curiosity about AI</li>
    </ul>
    ''', unsafe_allow_html=True)
