import streamlit as st
import requests

st.title("🦖 TREX Email Generator")

prompt = st.text_area("What do you want the email to say?")

tone = st.selectbox(
    "Choose tone",
    ["Professional", "Friendly", "Casual", "Apologetic", "Urgent"]
)

def generate_email(prompt, tone):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": f"""
You are TREX, an AI email assistant.

Write a {tone.lower()} email based on this:
{prompt}

Include subject and full email.
""",
            "stream": False
        }
    )
    return response.json()["response"]

if st.button("Generate Email"):
    if prompt:
        result = generate_email(prompt, tone)
        st.text_area("Your Email:", result, height=300)
    else:
        st.warning("Enter something first!")