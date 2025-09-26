import sys
import pandas as pd

if __name__ == "__main__":
    # args from dvc.yaml
    input_file = sys.argv[1]          # "zomato_df_final_data.csv"
    output_file = sys.argv[2]         # "data/processed/preprocessed.csv"

    # read -> very light clean -> write
    df = pd.read_csv(input_file)
    df = df.dropna()                  # minimal example; adjust as needed
    df.to_csv(output_file, index=False)

    print(f"Preprocessed data saved to {output_file}")
