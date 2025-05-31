
import streamlit as st
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler("usage.log"),
        logging.StreamHandler()
    ]
)

# Sidebar model selector
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ["Claude 3.5 Sonnet", "Claude v2", "DeepSeek-V2 Chat"]
)

model_id_map = {
    "Claude 3.5 Sonnet": "anthropic.claude-3-sonnet-20240620-v1:0",
    "Claude v2": "anthropic.claude-v2",
    "DeepSeek-V2 Chat": "deepseek.chat"
}

selected_model_id = model_id_map[model_choice]


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler("usage.log"),
        logging.StreamHandler()
    ]
)
from admin_panel import admin_settings_panel

st.set_page_config(page_title="Administrator Settings", layout="wide")

# Model selector (shared)
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ["Claude 3.5 Sonnet", "Claude v2", "DeepSeek-V2 Chat"]
)

model_id_map = {
    "Claude 3.5 Sonnet": "anthropic.claude-3-sonnet-20240620-v1:0",
    "Claude v2": "anthropic.claude-v2",
    "DeepSeek-V2 Chat": "deepseek.chat"
}

selected_model_id = model_id_map[model_choice]


st.title("⚙️ Administrator Control Panel")

model_id_map = {
    "Claude 3.5 Sonnet": "anthropic.claude-3-sonnet-20240620-v1:0",
    "Claude v2": "anthropic.claude-v2",
    "DeepSeek-V2 Chat": "deepseek.chat"
}

admin_settings_panel(model_id_map)