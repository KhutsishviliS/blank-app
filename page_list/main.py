import streamlit as st
from streamlit_app import page_design

# Define placeholder image
#placeholder_image = "https://via.placeholder.com/300"

# Get the selected language from session state
language = st.session_state.get('language', 'Georgian')

# Define project data with external/internal URLs
projects_1 = [
    {
        "title": {
            "Georgian": "პროექტი 1: Fashion MNIST ტანსაცმლის კლასიფიკატორი",
            "English": "Project 1: Fashion MNIST Clothing Classifier"
        },
        "description": {
            "Georgian": "ნეირონული ქსელის მოდელი, რომელიც ნავარჯიშებია MNIST-ის ტანისამოსის მონაცემთა ნაკრებზე, ტანსაცმლის სახეობების ავტომატური კლასიფიკაციის მიზნით.",
            "English": "A deep learning model trained on the Fashion MNIST dataset for clothing item classification."
        },
        "image": "images/tfcube1.webp",
        "url": "https://learndeeplearningwithsaba.streamlit.app/projects",
        "id": "001"
    },
    {
        "title": {
            "Georgian": "პროექტი 2: MNIST ციფრების კლასიფიკატორი",
            "English": "Project 2: MNIST Digit Classifier"
        },
        "description": {
            "Georgian": "ნეირონული ქსელის მოდელი რომელიც ნავარჯიშებია MNIST მონაცემთა ნაკრებზე, 0-დან 9-მდე ხელნაწერი ციფრების ავტომატური ამოცნობისა და კლასიფიკაციისთვის.",
            "English": "A deep learning model trained on the MNIST dataset for handwritten digit recognition."
        },
        "image": "images/tfcube2.webp",
        "url": "https://learndeeplearningwithsaba.streamlit.app/mnist",
        "id": "002"
    },
    {
        "title": {
            "Georgian": "პროექტი 3: სენტიმენტის ანალიზი",
            "English": "Project 3: Sentiment Analysis"
        },
        "description": {
            "Georgian": "ეს პროექტი განიხილავს მომხმარებლის შეფასებების სენტიმენტის ანალიზს.",
            "English": "This project performs sentiment analysis on user reviews using natural language processing techniques."
        },
        "image": "images/tfcube3.webp",
        "url": "https://learndeeplearningwithsaba.streamlit.app/mnist",
        "id": "003"
    }
]
button_name = {
    "Georgian":"იხილეთ გვერდი",
    "English":"Go to page"
}

# Page Title based on language
if language == 'Georgian':
    st.markdown("<h1 style='color:#3A485F;'>პროექტები ხელოვნურ ინტელექტში</h1>", unsafe_allow_html=True)
else:
    st.markdown("<h1 style='color:#3A485F;'>Projects in Artificial Intelligence</h1>", unsafe_allow_html=True)

# Introduction Text based on language
if language == 'Georgian':
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
else:
    st.markdown("""
    <style>
        .custom-text {
            color: #3A485F;
        }
    </style>
    <div class="custom-text">
        On this page, you will find various small projects in the field of artificial intelligence, which allow us to better understand what AI technology is. 
        The projects cover various topics such as data analysis, data processing and preparation, 
        and creating AI models based on existing data.
    </div>
    """, unsafe_allow_html=True)

if language == "Georgian":
    text = '''პროექტები დაწერილია 
            <a href="https://www.python.org/" style="text-decoration: none;">Python</a> 
            და 
            <a href="https://www.tensorflow.org/" style="text-decoration: none;">TensorFlow</a> 
            ბიბლიოთეკების გამოყენებით'''

else:
    text = '''Projects are written using 
            <a href="https://www.python.org/" style="text-decoration: none;">Python</a> 
            and 
            <a href="https://www.tensorflow.org/" style="text-decoration: none;">TensorFlow</a> 
            libraries'''

st.markdown(f"""
<p style="color:#3A485F;">
    {text}
</p>
""", unsafe_allow_html=True)

st.write("")

# Define the function to display a project
def display_project(title, description, image, url, id,button_name):
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
        <a href="{url}" target="_blank"><button class="button-{id}">{button_name}</button></a>
        """
        st.markdown(button_html, unsafe_allow_html=True)

# Loop through projects and display each one using the reusable function
for project in projects_1:
    display_project(
        title=project['title'][language],
        description=project['description'][language],
        image=project['image'],
        url=project['url'],
        id=project['id'],
        button_name = button_name[language]
    )
