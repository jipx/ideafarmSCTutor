# IdeaFarm SC Assistant for students and lecturers

This project is a multi-page Streamlit web application integrated with AWS Bedrock and Cognito. It includes an **Administrator Settings** panel for managing model selections, viewing logs, and analyzing API usage statistics.

---

## 🚀 Features

### ✅ Multi-Page Layout
- Home with app descriptions
- OWASP Top 10 vulnerability assistant
- WebGoat simulated testing
- Mimosa Secure Coding trainer
- Cloud Security assistant
- LLM Application Security
- Adaptive Quiz Generator
- Administrator Settings Panel (admin only)

### 🔐 Authentication
- OAuth2 login via **Amazon Cognito**
- Session-based role verification (admin access to settings)

### 🛠️ Administrator Features
- View and change model used by the app (Claude 3.5 Sonnet, Claude v2, DeepSeek)
- View last 2000 characters of log file (`admin.log`)
- View API usage stats from CSV (`usage_stats.csv`)
- Visualize daily usage with a line chart

---

## 📂 Project Structure

```
owasp_streamlit_app/
├── pages/
│   ├── 1_🔐_OWASP_Top_10.py
│   ├── 2_🛠️_WebGoat.py
│   ├── 3_🎓_Mimosa.py
│   ├── 4_☁️_Cloud_Security.py
│   ├── 5_🤖_LLM_App_Security.py
│   ├── 6_🧠_Adaptive_Quiz.py
│   └── 7_⚙️_Administrator_Settings.py
├── admin.log               # Optional log file
├── usage_stats.csv         # Optional usage stats CSV
├── Home.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run Locally

### 🖥️ Setup
1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd owasp_streamlit_app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add a `.streamlit/secrets.toml` file for Cognito credentials:
    ```toml
    COGNITO_DOMAIN = "https://<your-domain>.auth.<region>.amazoncognito.com"
    CLIENT_ID = "<client-id>"
    REDIRECT_URI = "http://localhost:8501"
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

---

## 📊 Sample Usage Stats Format

Sample `usage_stats.csv` format:
```csv
timestamp,user,action
2025-05-28T09:30:12Z,admin,Changed model
2025-05-28T10:02:01Z,admin,Viewed usage
```

---

## 🛡️ Built With

- [Streamlit](https://streamlit.io/)
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon Cognito](https://aws.amazon.com/cognito/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/) *(optional)*

---

## 📬 Contact

Sponsored by **Ideafarm @ Singapore Polytechnic**  
Maintained by: [Your Name or Team Name]  
For support, contact: [email@example.com]

---

## 🧯 Troubleshooting & Error Fixes

### ❌ Error: `StreamlitSetPageConfigMustBeFirstCommandError`

**Cause**: `st.set_page_config()` was not the first Streamlit command in the script.

**Fix**: Ensure it is the first command in each `.py` file (before `st.title()` or any `st.sidebar` call).

---

### ❌ Error: `KeyError` on model_id_map

**Cause**: Transformed keys (e.g., `.replace()` used on dropdown values) do not match actual dictionary keys.

**Fix**: Use `selected_model_id = model_id_map[model_choice]` without modifying `model_choice`.

---

### ❌ Error: `Missing Authentication Token` on API Gateway

**Cause**: Incorrect HTTP method or missing `/prod` stage in API endpoint.

**Fix**:
- Double-check the endpoint path in Postman.
- Use `POST` method if required.
- Ensure deployed stage (like `/prod`) is included in the URL.

---

### ❌ Error: `'EventStream' object is not subscriptable`

**Cause**: Attempting to parse response from Bedrock Agent Runtime using `response[...]` instead of streaming properly.

**Fix**: Iterate over the response like:
```python
for event in response["completion"]:
    print(event["content"])
```
Or use a simplified `.get("completion")` if response is pre-processed.

---

---

## 🚧 Pending Issues

### 🟠 AWS Bedrock Throttling

**Issue**: Users may experience `ThrottlingException` when calling `InvokeModel` on AWS Bedrock.

**Error Message**:
```
API Error 500
An error occurred (ThrottlingException) when calling the InvokeModel operation
```

**Cause**:
- You’ve exceeded your account’s provisioned throughput (TPS) for the selected model.
- Bedrock on-demand usage has strict regional limits.

**Workarounds**:
- Use a lower-rate model or reduce concurrent requests.
- Request a service quota increase from the AWS Console.
- Add a retry policy or exponential backoff in your code.

**Status**: A fix depends on AWS account configuration and quota approval.