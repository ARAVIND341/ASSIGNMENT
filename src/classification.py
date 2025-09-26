import sys, pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier

if __name__ == "__main__":
    inp = sys.argv[1]      # data/processed/features.csv
    out = sys.argv[2]      # models/classification_model.pkl

    df = pd.read_csv(inp)

    # 1) Choose/derive label
    if "is_popular" in df.columns:
        y = df["is_popular"]
    elif "rating_number" in df.columns:
        # derive a binary label from rating (adjust threshold if you like)
        y = (df["rating_number"] >= 4).astype(int)
    else:
        # fallback: all zeros (will trigger DummyClassifier)
        y = pd.Series([0]*len(df))

    # 2) Build numeric features, drop label columns if present
    X = df.drop(columns=[c for c in ["is_popular", "rating_number"] if c in df.columns], errors="ignore")
    X = X.select_dtypes(include=["number"]).fillna(0)

    # 3) Handle single-class case gracefully
    if y.nunique() < 2 or X.shape[1] == 0:
        clf = DummyClassifier(strategy="most_frequent")
        clf.fit([[0]]*len(y), y)  # minimal fit
    else:
        clf = LogisticRegression(max_iter=200)
        clf.fit(X, y)

    with open(out, "wb") as f:
        pickle.dump(clf, f)
    print(f"Classification model saved to {out}")
