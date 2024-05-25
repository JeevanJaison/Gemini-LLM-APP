from dotenv import load_dotenv
load_dotenv()   #load all the enviorment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# function to load gemini model and get responses
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(inputContent,image):
    if inputContent!="":
        response=model.generate_content([inputContent,image])
    else:
        response=model.generate_content(image)
    return response.text


st.set_page_config(page_title="Vision Demo")
st.header("Gemini Vision Application")
inputContent=st.text_input("Add instructions: ")

#Chatgpt
# File uploader to allow users to upload images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Optional: display the image format and size
    st.write(f"Format: {image.format}")
    st.write(f"Size: {image.size}")
    st.write(f"Mode: {image.mode}")

submit=st.button("Generate")

if submit:
    response=get_gemini_response(inputContent,image)
    st.subheader("The response is: ")
    st.write(response)