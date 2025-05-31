
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

st.set_page_config(page_title="OWASP Top 10", layout="wide")

st.title("🔐 OWASP Top 10")
st.markdown("Ask questions about the OWASP Top 10 security risks using the dropdown and prompt box below.")

# Model selector
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ["Claude 3.5 Sonnet", "Claude v2", "DeepSeek-V2 Chat"],
    key="model_selector_owasp"
)

model_id_map = {
    "Claude 3.5 Sonnet": "anthropic.claude-3-sonnet-20240620-v1:0",
    "Claude v2": "anthropic.claude-v2",
    "DeepSeek-V2 Chat": "deepseek.chat"
}

selected_model_id = model_id_map[model_choice]

# OWASP category selector
owasp_categories = [
    "A01: Broken Access Control",
    "A02: Cryptographic Failures",
    "A03: Injection",
    "A04: Insecure Design",
    "A05: Security Misconfiguration",
    "A06: Vulnerable and Outdated Components",
    "A07: Identification and Authentication Failures",
    "A08: Software and Data Integrity Failures",
    "A09: Security Logging and Monitoring Failures",
    "A10: Server-Side Request Forgery"
]

selected_category = st.selectbox("Select an OWASP Top 10 category", owasp_categories)

prompt = st.text_area("💬 Ask a question related to the selected category")

show_examples = st.checkbox("📚 Show sample vulnerable and mitigated code")

if st.button("Submit"):
    if not prompt:
        logging.info(f"[OWASP] Category: {selected_category} | Prompt: {prompt}")
        st.warning("Please enter a prompt.")
    else:
        example_suffix = (
            "\n\nAlso include a sample vulnerable code and a secure version of it in the answer."
            if show_examples else ""
        )
        full_prompt = f"Category: {selected_category}. Question: {prompt}{example_suffix}"
        with st.spinner("Contacting model..."):
            try:
                response = requests.post(
                    "https://5olh8uhg6b.execute-api.ap-northeast-1.amazonaws.com/prod/ask",
                    json={"prompt": full_prompt, "modelId": selected_model_id},
                    headers={"Content-Type": "application/json"}
                )
                result = response.json()
                output = result.get("response") or result.get("error") or "[No output returned]"
                if response.status_code == 200:
                    st.success("Model Response:")
                    st.markdown(output, unsafe_allow_html=True)
                else:
                    st.error(f"API Error {response.status_code}")
                    st.code(output)
            except Exception as e:
                st.error(f"Error contacting API: {e}")