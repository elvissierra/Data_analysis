from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from scraper.extractor_helpers import scrape_ticket_page, scrape_poi_main

BASE_TICKET_URL = "https://apollo-staging.geo.apple.com/tickets/kittyhawk-beta/"
BASE_POI_URL = "https://apollo-staging.geo.apple.com/p/release/"


def scrape_data(driver, row, tab_field_map):
    """
    Navigates to the correct page based on the input ID,
    then scrapes based on requested sections from the config.
    """
    results = {
        "MUIDs": row.get("MUIDs", ""),
        "Ticket IDs": row.get("Ticket IDs", ""),
        "Place IDs": row.get("Place IDs", "")
    }

    if row.get("Ticket IDs"):
        ticket_id = str(row["Ticket IDs"]).strip()
        driver.get(BASE_TICKET_URL + ticket_id)
        sleep(10)

        # Use global attribute map instead of per-row logic
        ticket_fields = tab_field_map.get("ToDo ticket page", [])
        if ticket_fields:
            results.update(scrape_ticket_page(driver, ticket_id, ticket_fields))
        else:
            results["Validation Notes"] = "No ticket fields requested"

    elif row.get("MUIDs") or row.get("Place IDs"):
        muid = str(row.get("MUIDs") or row.get("Place IDs")).strip()
        driver.get(BASE_POI_URL + muid)

        results.update(scrape_poi_main(driver, muid, tab_field_map))  # tab_field_map includes other tabs like Gemini, Versions, etc. if multiple tabs/columns in csv were selected

    else:
        results["Validation Notes"] = "No valid identifier provided"

    return results
