import sys
import pandas as pd

if __name__ == "__main__":
    # args from dvc.yaml

    # data - zomato_df_final_data.csv
    input_file = sys.argv[1]   
     # data - preprocessed.csv       
    output_file = sys.argv[2]        

    # reading,cleaning and writing operations
    df = pd.read_csv(input_file)
    df = df.dropna()                
    df.to_csv(output_file, index=False)

    print(f"Preprocessed data saved to {output_file}")
