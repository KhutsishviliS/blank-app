import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
import pickle5 as pickle

from streamlit_app import page_design

page_design()

language = st.session_state.get('language', 'Georgian')

@st.cache_resource
def load_mnist_model():
    try:
        with open('model/mnist_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        return loaded_model
        #model = tf.keras.models.load_model("model/mnist_model.h5")
        #return model
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

def process_image(image_data):
    # Convert the RGBA image to grayscale
    image = Image.fromarray(image_data.astype('uint8'), 'RGBA')
    image = ImageOps.grayscale(image)
    
    # Resize the image
    image = image.resize((28, 28))
    
    # Convert to numpy array and normalize
    image_array = np.array(image).astype('float32') / 255.0
    
    # Invert the colors (white digit on black background)
    image_array = 1 - image_array
    
    return image_array.reshape(1, 28, 28, 1), image

def predict_digit(model, image_array):
    try:
        prediction = model.predict(image_array)
        predicted_digit = prediction.argmax(axis=1)[0]
        confidence = prediction[0][predicted_digit]
        return predicted_digit, confidence
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return None, None

if language == "Georgian":
    st.markdown("""<h1 style="color:3A485F;">MNIST ციფრების კლასიფიკაცია</h1>""",unsafe_allow_html=True)
    st.markdown("""<p>დააგენერირეთ ციფრი ქვემოთ მოცემულ გრაფიკზე და იხილეთ პროგნოზი რეალურ დროში</p>""",unsafe_allow_html=True)
else:
    st.markdown("""<h1 style="color:3A485F;">MNIST Digit Classification Web App</h1>""",unsafe_allow_html=True)
    st.markdown("""<p style="color:3A485F;">Draw a digit on the canvas below and see real-time predictions</p>""",unsafe_allow_html=True)

model = load_mnist_model()

if model is not None:
    canvas_result = st_canvas(
        fill_color="#FFFFFF",
        stroke_width=20,
        stroke_color="#000000",
        background_color="#FFFFFF",
        update_streamlit=True,
        height=250,
        width=250,
        drawing_mode="freedraw",
        key="canvas"
    )

    if canvas_result.image_data is not None:
        # Check if the canvas is not empty (all black)
        if np.sum(canvas_result.image_data) > 0:
            image_array, processed_image = process_image(canvas_result.image_data)
            predicted_digit, confidence = predict_digit(model, image_array)

            if predicted_digit is not None:
                st.markdown(f"""<p style="color:#3A485F;">Predicted Digit: {predicted_digit}</p>""",unsafe_allow_html=True)
                st.markdown(f"""<p style="color:#3A485F;">Confidence: {confidence * 100:.2f}% </p>""",unsafe_allow_html=True)
                st.image(processed_image, caption="Processed Image (28x28)", width=100)
        else:
            st.write("Please draw a digit on the canvas.")
    else:
        st.write("Please draw a digit on the canvas.")
else:
    st.error("Failed to load the model. Please check the model path and try again.")