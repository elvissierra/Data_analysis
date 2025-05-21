import pandas as pd
import csv

"""def write_results(data):
    template_path = "Input_Config/config copy - Template.csv"
    output_path = "Output_Data/results.csv"

    try:
        # Load entire template (including metadata rows) without assigning header
        df = pd.read_csv(template_path, header=None)

        # Extract MUIDs header index (usually row 8, column 22)
        header_row_index = 8
        muid_column_name = "MUIDs"

        # Set actual column headers from header row
        df.columns = df.iloc[header_row_index]
        df = df.drop(index=list(range(0, header_row_index + 1)))  # Remove metadata rows
        df = df.reset_index(drop=True)

        # Fill in scraped data into the correct rows
        for entry in data:
            muid = str(entry.get("MUIDs")).strip()
            for i, row in df.iterrows():
                if str(row.get("MUIDs")).strip() == muid:
                    for key, value in entry.items():
                        if key != "MUIDs":
                            df.at[i, key] = value

        # Restore header and metadata rows from the original template
        original_template = pd.read_csv(template_path, header=None)
        output_df = pd.concat([
            original_template.iloc[:header_row_index + 1],  # keep original metadata rows
            df                                                   # processed data rows
        ], ignore_index=True)

        output_df.to_csv(output_path, index=False, header=False)
        print(f" Output written to {output_path}")

    except Exception as e:
        print(f"Failed to write results: {e}")"""

# Above is an attempt to format the results into a csv template that mirrors the formatting
# of the input template csv. Need to reexamine exactly how the data is shaped because I think
# I'm underestimating the complexity here. Below will just fill a blank CSV


import csv


def write_results(filepath, data):
    if not data:
        print("No data to write.")
        return

    fieldnames = list(data[0].keys())

    try:
        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Wrote raw scraped output to: {filepath}")
    except Exception as e:
        print(f"Failed to write output: {e}")
