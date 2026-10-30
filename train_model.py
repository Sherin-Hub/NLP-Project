from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

DATA = Path("data/messages.csv")
OUT = Path("models/scam_classifier.joblib")
df = pd.read_csv(DATA).dropna(subset=["text", "label"])
df["text"] = df["text"].astype(str)
df["label"] = df["label"].astype(str).str.lower().str.strip()
df = df[df["label"].isin(["scam", "legitimate"])]
if df["label"].nunique() < 2:
    raise ValueError("Dataset must contain both scam and legitimate labels.")

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.25, random_state=42, stratify=df["label"]
)
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), max_features=30000, sublinear_tf=True)),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))
])
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(classification_report(y_test, pred, zero_division=0))
print("Confusion matrix (labels: legitimate, scam):")
print(confusion_matrix(y_test, pred, labels=["legitimate", "scam"]))
OUT.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, OUT)
print(f"Saved model to {OUT}")
