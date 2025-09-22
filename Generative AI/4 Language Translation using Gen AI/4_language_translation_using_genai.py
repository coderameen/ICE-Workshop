import streamlit as st
import google.generativeai as genai
import os

#api setup
os.environ["GOOGLE_API_KEY"] = "YOUR GOOGLE GEMINI KEY HERE..."
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

#load pretrained model
model = genai.GenerativeModel('models/gemini-1.5-flash')

#app creation
def translate_language(input_text, target_language):
    prompt = f"""
    You are a Excellent Language translater please convert the below text into target language.

    Text: {input_text} to {target_language}

    """
    response = model.generate_content(prompt).text
    return response if response else "Translation Failed!"

st.title("Language Translation with GenAI")
input_text = st.text_area("Enter your text")
mylist = ['english','kannada','hindi']
target_language = st.selectbox("Choose target language", mylist)

if st.button("Translate"):
    if input_text.strip():#to avoid space/remove spaces
        result = translate_language(input_text, target_language)
        st.write(result)
