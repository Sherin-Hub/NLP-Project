# ScamShield – AI Scam Message Analyzer

A beginner-friendly NLP project using TF-IDF + Logistic Regression and a Streamlit interface.

## Important
The included CSV is a **tiny demo dataset**, created only to help you test the workflow. It is not suitable for real-world scam detection or reliable performance claims. Replace it with a larger, responsibly sourced, labeled dataset before evaluating the model seriously. The app's risk level is a simple heuristic, not a calibrated fraud probability.

## Requirements
- Python 3.10–3.12 recommended
- Internet connection for installing Python packages

## Setup (Windows)
1. Extract this ZIP folder.
2. Open the folder in VS Code.
3. Open Terminal → New Terminal.
4. Create and activate a virtual environment:

```bash
py -m venv .venv
.venv\Scripts\activate
```

5. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

6. Train the baseline model:

```bash
python train_model.py
```

7. Start Streamlit:

```bash
python -m streamlit run app.py
```

Your browser should open the local app. If not, copy the local URL shown in the terminal (usually `http://localhost:8501`).

## Project structure
- `app.py` – Streamlit interface
- `train_model.py` – trains and evaluates TF-IDF + Logistic Regression
- `src/analysis.py` – rule indicators and extracted entities
- `data/messages.csv` – small demo training dataset
- `models/` – trained model is created here after training

## Concepts demonstrated
Text classification, TF-IDF, preprocessing through the vectorizer, regex-based pattern extraction, basic rule-based indicators, model evaluation, and Streamlit UI.

## Next upgrades
1. Replace the demo data with a larger labeled dataset.
2. Add scam categories (phishing, impersonation, prize scam, job scam, etc.).
3. Add a pretrained/fine-tuned BERT classifier and compare metrics.
4. Improve entity extraction and explanation methods.
5. Test false positives and false negatives, and clearly show uncertainty.

## Safety
Do not paste real passwords, OTPs, bank details, or private messages containing sensitive information into demos. This project is educational and should not be used as the sole basis for deciding whether a message is safe.
