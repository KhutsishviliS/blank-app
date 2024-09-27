import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
import io

from streamlit_app import page_design

page_design()

language = st.session_state.get('language', 'Georgian')

@st.cache_resource
def load_custom_model():
    try:
        model = tf.keras.models.load_model("models/mnist_model2.h5")  # Adjust the model path
        return model
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

def process_image(image_data):
    """ Process image: Convert RGBA -> RGB, resize, and normalize """
    image = Image.fromarray(image_data.astype('uint8'), 'RGBA')
    image = image.convert("RGB")  # Convert to RGB
    
    # Resize to 244x244 as required by the models
    image = image.resize((244, 244))
    
    # Convert to numpy array and normalize between 0 and 1
    image_array = np.array(image).astype('float32') / 255.0
    
    return image_array.reshape(1, 244, 244, 3), image

def predict_digit(model, image_array):
    """ Perform the prediction on the processed image """
    try:
        prediction = model.predict(image_array)
        predicted_digit = prediction.argmax(axis=1)[0]
        confidence = prediction[0][predicted_digit]
        return predicted_digit, confidence
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return None, None

def convert_image_to_bytes(image):
    """ Convert PIL image to bytes for downloading """
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

# Page title and instructions based on language
if language == "Georgian":
    st.markdown("""<h1 style="color:#3A485F;">MNIST ციფრების კლასიფიკაცია</h1>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">აღნიშნული ნეირონული ქსელი ნავარჯიშებია სპეციალურად ამ პროექტისთვის შექმნილ მონაცემთა ნაკრებზე ჩრომელიც შედგება 500 ფოტო მონაცემისგან </p>""",unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">დააგენერირეთ ციფრი ქვემოთ მოცემულ გრაფიკზე და იხილეთ პროგნოზი რეალურ დროში</p>""", unsafe_allow_html=True)
else:
    st.markdown("""<h1 style="color:#3A485F;">MNIST Digit Classification Web App</h1>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">This neural network is trained on a custom dataset of 500 images, collected specifically for this project.</p>""",unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">Draw a digit on the canvas below and see real-time predictions</p>""", unsafe_allow_html=True)

# Load the custom model
model = load_custom_model()

if model is not None:
    # Drawing canvas settings
    canvas_result = st_canvas(
        fill_color="#FFFFFF",
        stroke_width=10,
        stroke_color="#000000",
        background_color="#FFFFFF",
        update_streamlit=True,
        height=350,
        width=750,
        drawing_mode="freedraw",
        key="canvas"
    )

    if canvas_result.image_data is not None:
        # Check if the canvas is not empty (all black)
        if np.sum(canvas_result.image_data) > 0:
            image_array, processed_image = process_image(canvas_result.image_data)
            predicted_digit, confidence = predict_digit(model, image_array)

            if predicted_digit is not None:
                st.markdown(f"""<p style="color:#3A485F;">Predicted Digit: {predicted_digit}</p>""", unsafe_allow_html=True)
                st.markdown(f"""<p style="color:#3A485F;">Confidence: {confidence * 100:.2f}% </p>""", unsafe_allow_html=True)
                st.image(processed_image, caption="Processed Image (244x244)", width=100)

                # Convert the processed image to bytes for downloading
                image_bytes = convert_image_to_bytes(processed_image)

                # Download button
                st.download_button(
                    label="Download Image",
                    data=image_bytes,
                    file_name="drawn_digit.png",
                    mime="image/png"
                )
        else:
            st.write("Please draw a digit on the canvas.")
    else:
        st.write("Please draw a digit on the canvas.")
else:
    st.error("Failed to load the model. Please check the model path and try again.")
