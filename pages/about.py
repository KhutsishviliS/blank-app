import streamlit as st
from streamlit_app import page_design

page_design()
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