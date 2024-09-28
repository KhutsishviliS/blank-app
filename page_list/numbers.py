import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import cv2

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
        # Predict and return the top prediction with its confidence
        prediction = model.predict(image_array)
        return prediction[0]  # Return the full prediction array for bar plot
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        return None

def convert_image_to_bytes(image):
    """ Convert PIL image to bytes for downloading """
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

def compute_saliency_map(model, image_array):
    """ Compute the saliency map """
    image_array = tf.convert_to_tensor(image_array)
    with tf.GradientTape() as tape:
        tape.watch(image_array)
        preds = model(image_array)
        top_pred_index = tf.argmax(preds[0])
        top_pred = preds[0][top_pred_index]

    grads = tape.gradient(top_pred, image_array)
    saliency = tf.reduce_max(tf.abs(grads), axis=-1).numpy()
    return saliency[0]

def display_saliency_on_image(image, saliency):
    """ Overlay the saliency map on the image with better visualization """
    # Normalize and apply a colormap to the saliency map
    saliency = saliency - saliency.min()
    saliency = saliency / saliency.max()  # Normalize to [0, 1]
    saliency = np.uint8(255 * saliency)  # Scale to [0, 255]
    
    # Convert the saliency to a heatmap using a colormap
    heatmap = cv2.applyColorMap(saliency, cv2.COLORMAP_JET)

    # Convert the image to a format compatible with OpenCV
    image_cv = np.array(image)

    # Blend the heatmap with the original image
    blended = cv2.addWeighted(image_cv, 0.6, heatmap, 0.4, 0)
    return Image.fromarray(blended)

# Page title and instructions based on language
if language == "Georgian":
    st.markdown("""<h1 style="color:#3A485F;">MNIST ციფრების კლასიფიკაცია</h1>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">აღნიშნული ნეირონული ქსელი ნავარჯიშებია სპეციალურად ამ პროექტისთვის შექმნილ მონაცემებზე რომელიც შედგება 500 ფოტო მონაცემისგან </p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">დააგენერირეთ ციფრი ქვემოთ მოცემულ გრაფიკზე და იხილეთ პროგნოზი რეალურ დროში</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">
                    Interpret button გვეხმარება გავიგოთ, თუ რის მიხედვიტ ახდენს მოდელი პროგნოზირებას. 
                    აპლიკაციაში იქმნება სპეციალურ ვიზუალურ რუკას, რომელიც გვიჩვენებს, თუ ნახატის რომელი ნაწილები იყო ყველაზე მნიშვნელოვანი მოდელის გადაწყვეტილებისთვის. 
                    ამგვარად, შეგვიძლიათ ვნახოთ, თუ რომელ მახასიათებლებზე გაამახვილა ყურადღება მოდელმა ჩვენს მიერ დახატული ციფრის იდენტიფიცირებისას.
                </p>
                """, unsafe_allow_html=True)
else:
    st.markdown("""<h1 style="color:#3A485F;">MNIST Digit Classification Web App</h1>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">This neural network is trained on a custom dataset of 500 images, collected specifically for this project.</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">Draw a digit on the canvas below and see real-time predictions</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color:#3A485F;">The Interpret button helps you understand how the model makes predictions. 
                When you click it, the app creates a special visual map that shows which parts of your drawing were most important for the model's decision. 
                This way, you can see what features the model focused on when identifying the digit you drew.</p>""",unsafe_allow_html=True)

# Load the custom model
model = load_custom_model()

if model is not None:
    # Place the 'Interpret' and 'Download Image' buttons side by side
    col_buttons = st.columns([1, 1])
    with col_buttons[0]:
        interpret_button_pressed = st.button("Interpret")
    with col_buttons[1]:
        download_button_pressed = False  # Initialize download button state

    # Create two equal columns for Canvas and Barplot with 1:1 ratio
    col1, col2 = st.columns(2)

    with col1:
        # Drawing canvas settings
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
            # Process and predict the drawn image
            image_array, processed_image = process_image(canvas_result.image_data)
            predictions = predict_digit(model, image_array)

            if predictions is not None:
                # Replace the existing bar plot section with Streamlit's built-in bar_chart
                with col2:
                    st.bar_chart(predictions)

                # Additional details below the canvas and bar plot
                st.markdown("### Results")

                # Display top prediction and confidence directly below the canvas
                top_pred_idx = np.argmax(predictions)
                top_class_confidence = predictions[top_pred_idx]
                st.markdown(f"""<p style="color:#3A485F;">Top Prediction: {top_pred_idx}</p>""", unsafe_allow_html=True)
                st.markdown(f"""<p style="color:#3A485F;">Confidence: {top_class_confidence * 100:.2f}% </p>""", unsafe_allow_html=True)

                # Convert the processed image to bytes for downloading
                image_bytes = convert_image_to_bytes(processed_image)

                # Download button next to Interpret
                with col_buttons[1]:
                    download_button_pressed = st.download_button(
                        label="Download Image",
                        data=image_bytes,
                        file_name="drawn_digit.png",
                        mime="image/png"
                    )

                # Display processed image below
                st.image(processed_image, caption="Processed Image (244x244)", width=100)

                # Interpret button behavior
                if interpret_button_pressed:
                    # Compute saliency map
                    try:
                        saliency_map = compute_saliency_map(model, image_array)

                        # Overlay saliency map on the processed image
                        saliency_image = display_saliency_on_image(processed_image, saliency_map)

                        # Display saliency image below the bar plot and canvas
                        st.image(saliency_image, caption="Saliency Map", use_column_width=True)
                    except Exception as e:
                        st.error(f"Error generating saliency map: {str(e)}")
