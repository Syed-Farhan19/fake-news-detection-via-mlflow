import streamlit as st
import requests


# Backend API URL
API_URL = "http://backend:8000/predict"

st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("Fake News Detection App")
st.write("Enter any news text below to check whether it is **REAL** or **FAKE**.")

# User input box
user_input = st.text_area("News Content", height=200, placeholder="Paste or write news text here...")

# Prediction button
if st.button("Predict"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Predicting..."):
            try:
                response = requests.post(API_URL, json={"text": user_input})
                
                if response.status_code == 200:
                    result = response.json()
                    label = result["prediction"]
                    confidence = result["confidence"]

                    st.success(f"Prediction: **{label}**")

                    if confidence is not None:
                        st.info(f"Confidence: {confidence:.2f}")

                else:
                    st.error("Error: Could not get a valid response from the backend.")
            
            except Exception as e:
                st.error(f"Failed to connect to backend API.\nError: {e}")
