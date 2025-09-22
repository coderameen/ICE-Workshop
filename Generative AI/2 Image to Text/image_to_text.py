import streamlit as st
import PIL.Image
import os 
import google.generativeai as genai
#API Setup
os.environ["GOOGLE_API_KEY"] = "YOUR GOOGLE GEMINI KEY HERE..."
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
#app creation
def image_to_text_generation(img,query):
    response = model.generate_content([query,img]).text
    return response

st.title("Image to Text Generation")
st.write("Upload an image to get details about it")

upload_image = st.file_uploader("Upload Image", type=['png','jpg','jpeg'])
query = st.text_input("what to want from the uploaded image")

if st.button("Generate"):
    if upload_image:
        img = PIL.Image.open(upload_image)
        result = image_to_text_generation(img,query)

        st.write(result)
