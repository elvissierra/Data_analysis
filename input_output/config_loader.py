import pandas as pd


def load_config(filepath):
    try:

        df = pd.read_csv(filepath, header=9)
        # Denoting that the real data starts on row 10, 9 is headers

        # Clean: drop rows where MUID is missing
        df = df.dropna(subset=["MUIDs"])
        df = df.fillna("")  # Replace any remaining NaNs with empty strings

        # Return rows as list of dictionaries (each row = one task)
        return df.to_dict(orient="records")

    except Exception as e:
        print(f"Failed to load config: {e}")
        return []
