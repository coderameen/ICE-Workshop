#pip install streamlit
import streamlit as st
import pickle
#load ml model
model  = pickle.load(open("model.pkl","rb"))

st.title("Pizza Prediction Application")

age = st.text_input("Enter your age: ")
weight = st.text_input("Enter your weight: ")

if st.button("Predict"):
    # st.write("Hello ICEans")
    if age and weight:
        pred = model.predict([[int(age),int(weight)]])
        # st.write(pred)
        if pred == 1:
            st.write("Eat Pizza and Enjoy!!")
        else:
            st.write("Go GYM brooh")
    else:
        st.error("Please provide input brother")