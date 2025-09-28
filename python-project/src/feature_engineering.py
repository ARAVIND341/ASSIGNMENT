import sys
import pandas as pd

if __name__ == "__main__":
    # input - preprocessed.csv
    input = sys.argv[1]     
    #output - features.csv
    out = sys.argv[2]      

    df = pd.read_csv(input)

  
    # filling missing numeric with the value 0
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    df[num_cols] = df[num_cols].fillna(0)

    # derived feature
    if {"cost", "votes"}.issubset(df.columns):
        df["cost_per_vote"] = df["cost"] / (df["votes"] + 1)

    df.to_csv(out, index=False)
    print(f"Features saved to {out}")
