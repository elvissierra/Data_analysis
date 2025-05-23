import pandas as pd


def load_config(filepath):
    try:
        id_columns = ["MUIDs", "Place IDs", "Ticket IDs"]
        df = pd.read_csv(filepath, header=9, dtype=str).fillna("")

        # Fix misnamed columns (e.g., "Unnamed: 22") → rename them properly
        df.columns = [str(col).strip() for col in df.columns]

        # Normalize column names for ID detection
        active_id_col = next((col for col in id_columns if col in df.columns and df[col].str.strip().any()), None)

        if not active_id_col:
            print(f"Failed to load config: no populated ID column found among {id_columns}")
            return [], None, df

        # Get IDs only — do NOT filter the whole DataFrame
        ids_to_scrape = df[active_id_col].dropna().astype(str).str.strip()
        ids_to_scrape = ids_to_scrape[ids_to_scrape != ""].tolist()

        return ids_to_scrape, active_id_col, df

    except Exception as e:
        print(f"Failed to load config: {e}")
        return [], None, pd.DataFrame()
    
def parse_tab_blocks(df):
    """
    Parses vertical tab blocks from the config csv:
    [Tab Header] | [Checkbox Column] | [Col Output Hint] → repeats per tab
    Returns: {
        "Place Details tab": ["Carto Score", "Name"],
        "Versions tab": ["Version ID", "Status"]
    }
    If Carto Score, Name, Version ID, and Status were checked on the csv.
    """
    tab_field_map = {}
    col_index = 0

    while col_index < len(df.columns) - 2:
        header_col = df.columns[col_index]
        checkbox_col = df.columns[col_index + 1]
        output_col = df.columns[col_index + 2]  # currently unused

        tab_name = str(header_col).strip()

        # Confirm it’s a tab block by reading csv headers
        if tab_name.endswith("tab") or tab_name == "ToDo ticket page":
            for i in range(df.shape[0]):
                attribute = str(df.iloc[i, col_index]).strip()
                checked = str(df.iloc[i, col_index + 1]).strip().lower()

                if attribute and checked in ["1", "true", "✓", "x"]:
                    if tab_name not in tab_field_map:
                        tab_field_map[tab_name] = []
                    tab_field_map[tab_name].append(attribute)

        col_index += 3  # skips to the next 3-column block
    print("THIS IS TAB FIELD MAP", tab_field_map) 


    return tab_field_map


def is_ticket_id_request(row):
    """
    Returns True if the 'ToDo ticket page' checkbox column is marked in this row.
    Assumes a 3-column repeating structure: [Tab Header] | [Checkbox] | [Output Col]
    """
    columns = list(row.keys())

    for i in range(len(columns) - 2):  # Look ahead safely
        if columns[i].strip() == "ToDo ticket page":
            checkbox_col = columns[i + 1]
            val = str(row.get(checkbox_col, "")).strip().lower()
            print("HEADER:", columns[i])
            print("CHECKBOX COL:", columns[i + 1])
            print("CHECKBOX VALUE:", row.get(columns[i + 1]))
            return val in ["true", "1", "x", "✓"]
    
    print("HEADER:", columns[i])
    print("CHECKBOX COL:", columns[i + 1])
    print("CHECKBOX VALUE:", row.get(columns[i + 1]))


    return False


def get_required_tabs_from_row(row):
    """
    Returns a list of tab names (e.g., 'Todos', 'Versions', etc.)
    that should be visited for this specific row.
    """
    COLUMN_TO_TAB = {
        "Place Details tab": "Gemini",
        "Versions tab": "Versions",
        "RAPs tab": "RAPs",
        "Edits tab": "Edits",
        "Todos Tab": "Todos",
        "ToDo ticket page": "Ticket"  # not a tab but special handler
    }

    required_tabs = set()
    col_index = 0
    columns = list(row.keys())

    while col_index < len(columns) - 2:
        header_col = columns[col_index]
        checkbox_col = columns[col_index + 1]

        tab_key = COLUMN_TO_TAB.get(header_col.strip())
        if not tab_key:
            col_index += 3
            continue  # Unknown or unsupported tab

        # Check if checkbox in this row is marked
        checked = str(row.get(checkbox_col, "")).strip().lower()
        if checked in ["1", "true", "✓", "x"]:
            required_tabs.add(tab_key)

        col_index += 3

    return list(required_tabs)









