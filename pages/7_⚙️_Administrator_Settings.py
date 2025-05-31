import streamlit as st
import logging
import os
import pandas as pd
from datetime import datetime

# ✅ Must be first
st.set_page_config(page_title="Administrator Settings", layout="wide")

# === Basic Role Check ===
if "role" in st.session_state and st.session_state["role"] != "admin":
    st.error("🚫 You do not have permission to view this page.")
    st.stop()

# === Logging ===
log_file = "admin.log"
logging.basicConfig(filename=log_file, level=logging.INFO)

st.title("⚙️ Administrator Settings")

# === Model Selector ===
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ["Claude 3.5 Sonnet", "Claude v2", "DeepSeek-V2 Chat"],
    key="model_selector_admin"
)

model_id_map = {
    "Claude 3.5 Sonnet": "anthropic.claude-3-sonnet-20240620-v1:0",
    "Claude v2": "anthropic.claude-v2",
    "DeepSeek-V2 Chat": "deepseek.chat"
}

selected_model_id = model_id_map[model_choice]
st.markdown(f"Model selected: **{model_choice}** (`{selected_model_id}`)")

# === Log Viewer ===
st.subheader("📄 Recent Logs")
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        st.code(f.read()[-2000:], language="text")
else:
    st.warning("No logs found yet.")

# === Usage Stats Viewer ===
st.subheader("📊 API Usage Stats")
usage_file = "usage_stats.csv"
if os.path.exists(usage_file):
    df = pd.read_csv(usage_file)
    st.dataframe(df)

    # === Usage Graph ===
    st.subheader("📈 Usage Chart")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['count'] = 1
    daily_usage = df.groupby(df['timestamp'].dt.date)['count'].sum()
    st.line_chart(daily_usage)
else:
    st.info("No usage statistics yet.")
