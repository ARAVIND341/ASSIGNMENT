import sys, pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    #features.csv
    inp = sys.argv[1]      
    #regression_model.pkl
    out = sys.argv[2]      

    df = pd.read_csv(inp)

    # Label + features
    y = df["rating_number"] if "rating_number" in df.columns else pd.Series([0]*len(df))
    X = df.drop(columns=[c for c in ["rating_number","is_popular"] if c in df.columns], errors="ignore")
    X = X.select_dtypes(include=["number"]).fillna(0)

    model = LinearRegression()
    model.fit(X, y)

    with open(out, "wb") as f:
        pickle.dump(model, f)
    print(f"Regression model saved to {out}")
