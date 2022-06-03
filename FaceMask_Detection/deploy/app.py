import streamlit as st
import requests

import streamlit as st
st.title("Image Classification for Mask Detection")

st.text("Upload an image with or without mask for image classification")

import keras
from PIL import Image, ImageOps
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np


def teachable_machine_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file)

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 120, 120, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (120, 120)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 255.0)

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability

uploaded_file = st.file_uploader("Choose an image ...", type="jpg")
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = teachable_machine_classification(image, 'cnn_mask.h5')
        if label == 1:
                st.write("Without Mask")
        else:
                st.write("With Mask")

