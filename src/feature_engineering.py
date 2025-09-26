import sys
import pandas as pd

if __name__ == "__main__":
    inp = sys.argv[1]      # data/processed/preprocessed.csv
    out = sys.argv[2]      # data/processed/features.csv

    df = pd.read_csv(inp)

    # --- minimal, safe feature examples (adjust to your columns) ---
    # Fill missing numeric with 0 to keep it simple
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    df[num_cols] = df[num_cols].fillna(0)

    # Simple derived feature (only if columns exist)
    if {"cost", "votes"}.issubset(df.columns):
        df["cost_per_vote"] = df["cost"] / (df["votes"] + 1)

    df.to_csv(out, index=False)
    print(f"Features saved to {out}")
