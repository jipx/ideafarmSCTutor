
import streamlit as st
import requests
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler("usage.log"),
        logging.StreamHandler()
    ]
)

st.set_page_config(page_title="Adaptive Quiz", layout="wide")

st.title("🧠 Adaptive Quiz Generator")

difficulty = st.selectbox("Choose difficulty", ["Beginner", "Intermediate", "Advanced"])
topic = st.text_input("Quiz Topic (e.g., XSS, IAM, Prompt Injection)")

if st.button("Generate Quiz Question"):
    quiz_prompt = f"Generate a {difficulty.lower()} level multiple choice question on {topic}. Include 4 options and indicate the correct answer."
    with st.spinner("Generating quiz..."):
        try:
            response = requests.post(
                "https://lkb0sv5un2.execute-api.ap-northeast-1.amazonaws.com/prod/invoke",
                json={"input": quiz_prompt},
                headers={"Content-Type": "application/json"}
            )
            result = response.json()
            output = result.get("completion") or "[No output returned]"
            st.markdown(output, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")