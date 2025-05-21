from input_output.config_loader import load_config
from input_output.output_writer import write_results
from scraper.browser_manager import start_driver
from scraper.extractor import scrape_ticket_data
from datetime import datetime


def run_app():
    print("--STARTING POI VALIDATION SCRIPT--")

    config_data = load_config(
        "Input_Config/config.csv"
    )  # config_copy.csv for testing purposes
    # Loads tickets and requested fields from input config doc

    print(f"🔢 Loaded {len(config_data)} rows from config.csv")

    driver = start_driver()
    # Starts the selenium browser session

    input(
        "Log in and then press enter to continue"
    )  # logging in manually for testing phase

    results = []

    for row in config_data:
        MUID = row["MUIDs"]
        print(f"Processing {MUID}")
        print(f"📄 Row MUID: {row.get('MUIDs')}")

        ticket_data = scrape_ticket_data(driver, MUID, row)
        results.append(ticket_data)

    # write_results("results.csv", results)
    # Above is for more complex results csv. Will think about later. Below is bandaid into empty csv

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    write_results(f"Output_Data/raw_results_{timestamp}.csv", results)

    print("Test run complete, hopefully")
