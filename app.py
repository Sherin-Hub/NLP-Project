
import streamlit as st
from pathlib import Path
import joblib
from src.analysis import analyze_message

st.set_page_config(page_title="ScamShield AI", page_icon="🛡️")

st.markdown("""
<style>
.stApp {background:linear-gradient(135deg,#0b1220,#172b4d);color:white}
.block-container {max-width:800px;padding-top:35px}
h1,h2,h3,p,label {color:white!important}
textarea {background:#111c30!important;color:white!important}
.stButton button {background:#3978f6;color:white;border:0;
border-radius:10px;padding:12px;font-weight:bold}
.stButton button:hover {background:#255bd0;color:white}
[data-testid="stMetric"] {background:#1c2e4b;padding:15px;
border-radius:12px}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ ScamShield AI")
st.caption("Smart Scam Detection Using Machine Learning & NLP")
st.divider()

model_path = Path("models/scam_classifier.joblib")
model = joblib.load(model_path) if model_path.exists() else None

st.subheader("🔍 Analyze Suspicious Messages")
message = st.text_area("Enter SMS, Email or Chat Message",
                       height=150, placeholder="Paste your message here...")

if st.button("🚀 Analyze Message", use_container_width=True):
    if not message.strip():
        st.warning("Please enter a message!")
    elif model is None:
        st.error("Model missing! Run: py train_model.py")
    else:
        result = analyze_message(message, model)
        prediction = str(result["prediction"])
        risk = str(result["risk"])
        indicators = result["indicators"]
        urls = result["urls"]
        keywords = ["urgent", "otp", "winner", "prize",
                    "password", "verify", "bank", "click"]
        found = [w for w in keywords if w in message.lower()]

        st.divider()
        st.subheader("📊 AI Analysis Results")
        col1, col2 = st.columns(2)
        col1.metric("Prediction", prediction)
        col2.metric("Risk Level", risk)

        st.subheader("🚦 Visual Risk Meter")
        risk_text = risk.lower()
        if "high" in risk_text:
            score, color = 90, "🔴 High Risk"
        elif "medium" in risk_text or "moderate" in risk_text:
            score, color = 55, "🟠 Medium Risk"
        else:
            score, color = 20, "🟢 Low Risk"
        st.write(color)
        st.progress(score)
        st.caption("Illustrative risk level, not a fraud probability.")

        st.subheader("🔗 Suspicious Link Detection")
        if urls:
            for url in urls:
                st.warning(f"Detected URL: {url}")
        else:
            st.success("No links detected.")

        st.subheader("🔑 Keyword Detection")
        if found:
            st.warning("Warning keywords: " + ", ".join(found))
        else:
            st.success("No configured warning keywords found.")

        if indicators:
            st.subheader("⚠️ Warning Indicators")
            for item in indicators:
                st.write("•", item)

        st.subheader("💡 Scam Prevention Tips")
        st.info("🔐 Never share OTPs, passwords or bank details.")
        st.info("🔗 Avoid clicking unknown or suspicious links.")
        st.info("📞 Verify unexpected requests through official channels.")

st.divider()
st.caption("ScamShield AI | Educational Project | Python + NLP + ML")
