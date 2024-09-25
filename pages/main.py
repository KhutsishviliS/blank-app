import streamlit as st
from streamlit_app import page_design

# Define placeholder image
placeholder_image = "https://via.placeholder.com/300"

# Define project data with external/internal URLs
projects_1 = [
    {
        "title": "Project 1: Fashion MNIST Clothing Classifier",
        "description": "This project involves analyzing the performance of various financial portfolios.",
        "image": "images/tfcube1.webp",
        "url": "https://learndeeplearningwithsaba.streamlit.app/projects",  # Link to an external or internal page
        "id": "001"
    },
    {
        "title": "Project 2: MNIST Digit Classifier",
        "description": "A deep learning model trained on the MNIST dataset for handwritten digit recognition.",
        "image": "images/tfcube2.webp",
        "url": "https://example.com/mnist",  # Link to another page
        "id": "002"
    },
    {
        "title": "Project 3: Sentiment Analysis",
        "description": "This project performs sentiment analysis on user reviews using natural language processing techniques.",
        "image": "images/tfcube3.webp",
        "url": "https://learndeeplearningwithsaba.streamlit.app/mnist",  # Link to another page
        "id": "003"
    }
]

# Page Title
st.markdown("<h1 style='color:#3A485F;'>პროექტები ხელოვნურ ინტელექტში</h1>", unsafe_allow_html=True)

# Introduction Text
st.markdown("""
<style>
    .custom-text {
        color: #3A485F;
    }
</style>

<div class="custom-text">
    ამ გვერდზე თქვენ ნახავთ სხვადასხვა მცირე პროექტებს ხელოვნური ინტელექტის მიმართულებით, რომლებიც საშუალებას გვაძლევენ უკეთ გავიგოთ თუ რა არის AI
    ტექნოლოგია. პროექტები მოიცავს სხვადასხვა თემატიკას, როგორიცაა მონაცემთა ანალიზი, მონაცემთა დამუშავება და მომზადება,
    ხელოვნური ინტელექტის მოდელების შექმნა არსებული მონაცემებით.
</div>
""", unsafe_allow_html=True)
st.markdown("""
<p style="color:#3A485F;">
    პროექტები დაწერილია 
    <a href="https://www.python.org/"  text-decoration: none;">Python</a> 
    და 
    <a href="https://www.tensorflow.org/"  text-decoration: none;">TensorFlow</a> 
    -ს გამოყენებით
</p>
""", unsafe_allow_html=True)

st.write("")

# Define the function to display a project
def display_project(title, description, image, url, id):
    col1, col2 = st.columns([1, 2])
    
    # Add project image on the left
    with col1:
        st.image(image, width=150)
    
    # Add project details and styled button on the right
    with col2:
        # Custom styling for title and description
        st.markdown(f"<h3 style='color:#3A485F;'>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#3A485F;'>{description}</p>", unsafe_allow_html=True)
        
        # Use st.markdown to create a styled button that links to an external or internal URL
        button_html = f"""
        <style>
        .button-{id} {{
            background-color: #FE6F00;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 5px;
            border: none;
            transition: background-color 0.3s ease;
        }}
        .button-{id}:hover {{
            background-color: #D65A00;
        }}
        </style>
        <a href="{url}" target="_blank"><button class="button-{id}">იხილეთ ლინკი</button></a>
        """
        st.markdown(button_html, unsafe_allow_html=True)

# Loop through projects and display each one using the reusable function
for project in projects_1:
    display_project(
        title=project['title'],
        description=project['description'],
        image=project['image'],
        url=project['url'],
        id=project['id']
    )
