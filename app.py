import streamlit as st
from pathlib import Path
import joblib
from src.analysis import analyze_message

st.set_page_config(page_title="ScamShield | AI Scam Analyzer", page_icon="🛡️", layout="centered")
st.title("🛡️ ScamShield")
st.subheader("AI Scam Message Analyzer")
st.caption("Analyze suspicious SMS, emails, and chat messages. Results are risk indicators—not proof that a message is a scam.")

MODEL_PATH = Path("models/scam_classifier.joblib")
model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None

message = st.text_area("Paste a message to analyze", height=200, placeholder="Example: Congratulations! You won a prize. Pay a fee to claim it...")
if st.button("🔎 Analyze message", type="primary", use_container_width=True):
    if not message.strip():
        st.warning("Please enter a message first.")
    elif model is None:
        st.error("Model not found. First run: python train_model.py")
    else:
        result = analyze_message(message, model)
        st.divider()
        st.subheader("Analysis result")
        st.metric("Prediction", result["prediction"])
        st.metric("Risk indicator", result["risk"])
        st.write("**Why this message was flagged**")
        if result["indicators"]:
            for item in result["indicators"]:
                st.write(f"- {item}")
        else:
            st.write("No configured warning patterns were detected.")
        st.write("**Extracted details**")
        st.write("**URLs:**", ", ".join(result["urls"]) if result["urls"] else "None detected")
        st.write("**Phone numbers:**", ", ".join(result["phones"]) if result["phones"] else "None detected")
        st.write("**Money amounts:**", ", ".join(result["money"]) if result["money"] else "None detected")
        st.info("**Safe next steps:** Don't click unexpected links or share OTPs, passwords, or banking details. Verify the sender through an official channel. If you already sent money, contact your bank promptly.")
