import streamlit as st
import google.generativeai as genai
import os

# 🔑 Configure Google API Key
os.environ["GOOGLE_API_KEY"] = "YOUR GOOGLE GEMINI KEY HERE..."
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Function to classify URL
def url_detection(url):
    prompt = f"""
    You are an advanced AI model specializing in URL security classification. Analyze the given URL and classify it as one of the following categories:

    1. benign: Safe, trusted, and non-malicious websites such as google.com, wikipedia.org, amazon.com.
    2. phishing: Fraudulent websites designed to steal personal information.
    3. malware: URLs that distribute viruses, ransomware, or malicious software.
    4. defacement: Hacked or defaced websites displaying unauthorized content.

    **Input URL:** {url}

    **Output Format:**  
    - Return only the class name in lowercase (benign, phishing, malware, defacement).
    """

    response = model.generate_content(prompt)
    return response.text.strip() if response else "Detection failed."


# 🎯 Streamlit App
st.title("🔎 URL Security Classifier")

st.write("Enter a URL below to classify it as **benign, phishing, malware, or defacement**.")

# Take URL input
url = st.text_input("Enter a URL:")

# Predict when button clicked
if st.button("Classify URL"):
    if not url:
        st.error("⚠️ Please enter a URL.")
    elif not url.startswith(("http://", "https://")):
        st.error("⚠️ Invalid URL format. Must start with http:// or https://")
    else:
        classification = url_detection(url)
        st.success(f"Prediction: **{classification}**")
