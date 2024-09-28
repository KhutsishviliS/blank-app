import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import pandas as pd

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
    image = image.convert("RGB")  
    
    # Resize image to match model input dimensions (244x244 in this case)
    image = image.resize((244, 244))
    
    # Normalize image array and reshape it for the model
    image_array = np.array(image).astype('float32') / 255.0
    return image_array.reshape(1, 244, 244, 3), image

def predict_digit(model, image_array):
    """ Perform the prediction on the processed image """
    try:
        # Predict and return the top 5 predictions with their confidence
        prediction = model.predict(image_array)
        top_5_indices = np.argsort(prediction[0])[-5:][::-1]  # Top 5 predictions
        top_5_confidences = prediction[0][top_5_indices]
        return top_5_indices, top_5_confidences
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
    st.markdown("""<p style="color:#3A485F;">აღნიშნული ნეირონული ქსელი ნავარჯიშებია სპეციალურად ამ პროექტისთვის შექმნილ მონაცემებზე რომელიც შედგება 500 ფოტო მონაცემისგან </p>""",unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">დააგენერირეთ ციფრი ქვემოთ მოცემულ გრაფიკზე და იხილეთ პროგნოზი რეალურ დროში</p>""", unsafe_allow_html=True)
else:
    st.markdown("""<h1 style="color:#3A485F;">MNIST Digit Classification Web App</h1>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">This neural network is trained on a custom dataset of 500 images, collected specifically for this project.</p>""",unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">Draw a digit on the canvas below and see real-time predictions</p>""", unsafe_allow_html=True)

# Load the custom model
model = load_custom_model()

if model is not None:
    # Drawing canvas settings (no columns, just the canvas first)
    canvas_result = st_canvas(
        fill_color="#FFFFFF",
        stroke_width=10,
        stroke_color="#000000",
        background_color="#FFFFFF",
        update_streamlit=True,
        height=350,
        width=350,
        drawing_mode="freedraw",
        key="canvas"
    )

    if canvas_result.image_data is not None:
        # Check if the canvas is not empty (all black)
        if np.sum(canvas_result.image_data) > 0:
            image_array, processed_image = process_image(canvas_result.image_data)
            top_5_indices, top_5_confidences = predict_digit(model, image_array)

            if top_5_indices is not None:
                # Display processed image and prediction results
                st.markdown(f"""<p style="color:#3A485F;">Top Prediction: {top_5_indices[0]}</p>""", unsafe_allow_html=True)
                st.markdown(f"""<p style="color:#3A485F;">Confidence: {top_5_confidences[0] * 100:.2f}% </p>""", unsafe_allow_html=True)
                
                st.image(processed_image, caption="Processed Image (244x244)", width=100)

                # Convert the processed image to bytes for downloading
                image_bytes = convert_image_to_bytes(processed_image)

                # Download button for the processed image
                st.download_button(
                    label="Download Image",
                    data=image_bytes,
                    file_name="drawn_digit.png",
                    mime="image/png"
                )

                # Prepare data for the horizontal bar chart
                prediction_data = pd.DataFrame({
                    'Prediction': top_5_indices,
                    'Confidence': top_5_confidences
                })

                # Plot top 5 predictions using Streamlit's built-in plotting function
                st.bar_chart(prediction_data.set_index('Prediction'))
        else:
            st.write("Please draw a digit on the canvas.")
    else:
        st.write("Please draw a digit on the canvas.")
else:
    st.error("Failed to load the model. Please check the model path and try again.")
