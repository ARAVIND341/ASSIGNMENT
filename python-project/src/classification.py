import sys, pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier

if __name__ == "__main__":

    #features.csv
    input = sys.argv[1] 
    #classification_model.pkl
    out = sys.argv[2]      

    df = pd.read_csv(input)

    # deriving label
    if "is_popular" in df.columns:
        y = df["is_popular"]
    elif "rating_number" in df.columns:
        # getting a binary label
        y = (df["rating_number"] >= 4).astype(int)
    else:
        y = pd.Series([0]*len(df))

    # builing features numeric in nature
    X = df.drop(columns=[c for c in ["is_popular", "rating_number"] if c in df.columns], errors="ignore")
    X = X.select_dtypes(include=["number"]).fillna(0)

    # single class
    if y.nunique() < 2 or X.shape[1] == 0:
        clf = DummyClassifier(strategy="most_frequent")
        clf.fit([[0]]*len(y), y)  # minimal fit
    else:
        clf = LogisticRegression(max_iter=200)
        clf.fit(X, y)

    with open(out, "wb") as f:
        pickle.dump(clf, f)
    print(f"Classification model saved to {out}")
