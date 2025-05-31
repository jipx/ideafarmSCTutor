
import streamlit as st

st.set_page_config(page_title="OWASP AI Assistant", layout="wide")

st.title("🔐 OWASP AI Assistant")
st.markdown("Welcome to the OWASP AI Assistant. Use the sidebar or the cards below to explore each module.")

st.header("📘 Application Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔐 OWASP Top 10")
    st.write("Explore the top web security risks.")
    st.button("Go to OWASP Top 10", key="owasp")

with col2:
    st.markdown("### 🛠️ WebGoat")
    st.write("Practice with deliberately vulnerable apps.")
    st.button("Go to WebGoat", key="webgoat")

with col3:
    st.markdown("### 🎓 Mimosa (Tutor)")
    st.write("Analyze secure coding assessments.")
    st.button("Go to Mimosa", key="mimosa")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("### ☁️ Cloud Security")
    st.write("Review cloud-specific security practices.")
    st.button("Go to Cloud Security", key="cloud")

with col5:
    st.markdown("### 🤖 LLM App Security")
    st.write("Investigate risks in AI applications.")
    st.button("Go to LLM App Security", key="llm")

with col6:
    st.markdown("### 🧠 Adaptive Quiz")
    st.write("Take dynamically generated quizzes.")
    st.button("Go to Adaptive Quiz", key="quiz")

st.markdown("---")
st.markdown("Built with ❤️ using Amazon Bedrock, Streamlit, and OWASP guidance.")
