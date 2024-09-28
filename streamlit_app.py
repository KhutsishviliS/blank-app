import streamlit as st
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
if 'language' not in st.session_state:
    st.session_state['language'] = 'Georgian'  # Set default language to Georgian

language = st.selectbox("Choose Language ", ["Georgian", "English"])

# Store the selected language in session state
st.session_state['language'] = language

###############################################
about = st.Page(
    page="page_list/about.py",
    title="About Me",
    icon="🧑"
)
project = st.Page(
    page="page_list/projects.py",
    title="Fashion MNIST",
    icon="📚"
)

main_page = st.Page(
    page="page_list/main.py",
    title="Main Page",
    icon="🤖",
    default=True
)
# digit_mnist = st.Page(
#     page="page_list/mnist.py",
#     title="MNIST Digit Classifier",
#     icon="📚"
# )

number_classification = st.Page(
    page="page_list/numbers.py",
    title = "Try it out",
    icon= "📺"

)
# ----------- NAVIGATION ----------- #
pg = st.navigation(pages=[main_page, project, number_classification, about])#,contact_page digit_mnist,
pg.run()
