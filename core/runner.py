from input_output.config_loader import load_config, parse_tab_blocks
from input_output.output_writer import write_results
from scraper.browser_manager import start_driver
from scraper.extractor import scrape_data
from datetime import datetime
from time import sleep


def run_app():
    print("--STARTING POI VALIDATION SCRIPT--")

    # Load IDs, ID type (e.g., 'Tickets'), and full DataFrame
    ids, id_type, full_df = load_config("Input_Config/config.csv")

    print(f"Loadedd {len(ids)} IDs from config.csv using column: {id_type}")

    if not ids:
        print("No valid IDs to scrape, exiting.")
        return

    # Extract checked attributes globally from the full config
    tab_field_map = parse_tab_blocks(full_df)

    driver = start_driver()
    print("5 sec wait until scrape starts")
    sleep(5)

    results = []

    for id_val in ids:
        # Construct a synthetic "row" for this ID
        row = {id_type: id_val}

        # Pass full tab/field map + current ID to scrape_data
        data = scrape_data(driver, row, tab_field_map)
        results.append(data)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write_results(f"Output_Data/raw_results_{timestamp}.csv", results)

    print("✅ Test run complete")
