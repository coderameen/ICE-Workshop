import streamlit as st
import google.generativeai as genai
import os
#To loading/preprocessing image
import PIL.Image

# Set api key

os.environ['GOOGLE_API_KEY']= "YOUR GOOGLE GEMINI KEY HERE..."
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

#Load the pre-trained model/llm model/genai model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


#Custom funtions
def analyze_human_attributes(img):
    prompt = """
    You are an AI Trained to analyze human attributes from images with high accuracy.
    Carefully analyze the given image and return the following structured details:
    
    You have to return all results as you have the image, don't want any apologize or empty
    
    - **Gender** (Male/Female/Non-binary)
    - **Age Estimate** (e.g., 25 years)
    - **Ethnicity** (e.g., Asian, Caucasian, African, etc.)
    - **Mood** (e.g., Happy, sad, Neutral, Excited)
    - **Facial Expression** (e.g., Smiling, Frowning, Neutral, etc.)
    - **Glasses** (Yes/No)
    - **Beard** (Yes/No)
    - **Hair Color** (Black, Blonde, Brown)
    - **Eye Color** (e.g., Blue, Gree, Black, brown)
    - **Head Wear** (Yes/No, specify type if applicable)
    - **Emotion Detected** (e.g., Joyful, Focused, Angry, etc.,)
    - **Confidence level** (Accuracy of prediction in percentage)
    """
    response = model.generate_content([prompt,img])
    return response.text.strip()


#APP Creation
st.title("Human Attribute Detection")
st.write("Upload an Image to detect attributes...")

#Image upload
uploaded_image = st.file_uploader("Upload an Image", type=['png','jpg','jpeg'])
if uploaded_image:
    img = PIL.Image.open(uploaded_image)
    
    #pass image to model
    person_info = analyze_human_attributes(img)
    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, caption='Uploaded image', use_container_width=True)
    with col2:
        st.write(person_info)
        
