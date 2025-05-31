import streamlit as st
import requests
import logging
import json
import streamlit.components.v1 as components

logging.basicConfig(level=logging.INFO)

def speak_text(text):
    js = f"""
    <script>
        var utterance = new SpeechSynthesisUtterance({json.dumps(text)});
        utterance.lang = 'en-US';
        window.speechSynthesis.speak(utterance);
    </script>
    """
    components.html(js)

st.title("🎓 Mimosa (for tutor only)")

model_choice = st.sidebar.selectbox(
    "Choose a model",
    ["Claude 3.5 Sonnet", "Claude v2", "DeepSeek-V2 Chat"],
    key="model_selector_mimosa"
)

model_id_map = {
    "Claude 3.5 Sonnet": "anthropic.claude-3-sonnet-20240620-v1:0",
    "Claude v2": "anthropic.claude-v2",
    "DeepSeek-V2 Chat": "deepseek.chat"
}

selected_model_id = model_id_map[model_choice]

prompt = st.text_area("Enter your secure coding or grading-related question")
if st.button("Submit"):
    logging.info("[Mimosa] Prompt: " + prompt)
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Contacting model..."):
            try:
                response = requests.post(
                    "https://5olh8uhg6b.execute-api.ap-northeast-1.amazonaws.com/prod/ask",
                    json={"prompt": prompt, "modelId": selected_model_id},
                    headers={"Content-Type": "application/json"}
                )
                result = response.json()
                output = result.get("response") or result.get("error") or "[No output returned]"
                if response.status_code == 200:
                    st.success("Model Response:")
                    st.markdown(output, unsafe_allow_html=True)
                    if st.button("🔊 Read aloud", key="read_response_mimosa"):
                        speak_text(output)
                else:
                    st.error(f"API Error {response.status_code}")
                    st.code(output)
            except Exception as e:
                st.error(f"Error contacting API: {e}")
