from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from input_output.config_loader import get_required_tabs_from_row
from scraper.tab_nav import click_tab
from scraper.tab_ticket_scrapers import edits_tab, gemini_tab, raps_tab, ticket_page, todos_tab, versions_tab 


#Stores attributes that were checked off on csv file. 

def get_requested_fields_for_tab(row, tab):
    """
    Returns the list of fields under the given tab (e.g. 'Gemini') that are checked in this row.
    """
    TAB_TO_HEADER = {
        "Gemini": "Place Details tab",
        "Versions": "Versions tab",
        "Todos": "Todos tab",
        "RAPs": "RAPs tab",
        "Edits": "Edits tab"
    }

    header = TAB_TO_HEADER.get(tab)
    if not header:
        return []

    fields = []
    columns = list(row.keys())

    for i in range(len(columns) - 2):
        if columns[i].strip() == header:
            checkbox_col = columns[i + 1]
            field_label = str(row.get(columns[i], "")).strip()
            checkbox_value = str(row.get(checkbox_col, "")).strip().lower()
            #Checks to see how quip/numbers/wherever the csv came from defines the value of a checkmark box. Once confirmed, appends checkmarked fields to attribute list
            if checkbox_value in ["✓", "x", "true", "1"] and field_label:
                fields.append(field_label)

    return fields


#Stores attributes that were checked off on csv file, but only for the ToDo ticket page column
def get_requested_fields_for_ticket_page(row):
    """
    Returns a list of fields requested under the 'ToDo ticket page' block.
    Assumes 3-column structure: [Tab Header] | [Checkbox] | [col]
    """
    fields = []
    columns = list(row.keys())

    for i in range(len(columns) - 2):
        if columns[i].strip() == "ToDo ticket page":
            checkbox_col = columns[i + 1]
            field_label = str(row.get(columns[i], "")).strip()
            checkbox_val = str(row.get(checkbox_col, "")).strip().lower()

            if checkbox_val in ["✓", "x", "true", "1"] and field_label:
                fields.append(field_label)

    return fields



def scrape_poi_main(driver, muid, tab_field_map):
    """
    Scrapes the POI main page based on which tab fields are requested.
    Always begins on the default 'Gemini' tab (Place Details).
    """
    results = {}

    for tab, fields in tab_field_map.items():
        if not fields:
            continue

        if tab == "Gemini" or "Place Details tab":
            results.update(gemini_tab.scrape(driver, fields))
        elif tab == "Todos":
            click_tab(driver, tab)
            results.update(todos_tab.scrape(driver, fields))
        elif tab == "Versions":
            click_tab(driver, tab)
            results.update(versions_tab.scrape(driver, fields))
        elif tab == "RAPs":
            click_tab(driver, tab)
            results.update(raps_tab.scrape(driver, fields))
        elif tab == "Edits":
            click_tab(driver, tab)
            results.update(edits_tab.scrape(driver, fields))
        # Add more tabs as needed

    return results



def scrape_ticket_page(driver, ticket_id, requested_fields):
    """
    Scrapes the standalone Ticket page.
    Only called if global tab_field_map contains fields under 'ToDo ticket page'.
    """
    if requested_fields:
        return ticket_page.scrape(driver, requested_fields)
    return {}



