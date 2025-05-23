# POI Validation Automation Project Documentation

## Overview

This project automates the validation of Points of Interest (POIs) and ToDo tickets using Selenium. It reads from a Quip-exported configuration CSV, navigates to either a Ticket page or a POI (MUID/Place ID) page, and scrapes the required data fields based on user-specified checkboxes in the spreadsheet.

---

## File Structure

```
Analysis_Automation_Project/
├── run.py                          # Main script to execute the scraper
├── README.md                       # Project overview and setup guide
├── requirements.txt                # Python package dependencies
├── scaffold.md                     # Project planning scaffold (optional)
│
├── core/
│   ├── main.py                     # Entrypoint logic
│   └── runner.py                   # Orchestration and main application loop
│
├── Input_Config/
│   ├── config.csv                  # Primary Quip-exported spreadsheet
│   └── config copy - Template.csv  # Field selection template for reuse
│
├── input_output/
│   ├── config_loader.py            # Reads config and extracts scrape targets
│   └── output_writer.py            # Saves results to CSV
│
├── Output_Data/
│   └── results.csv                 # Final scraped data output
│
├── scraper/
│   ├── browser_manager.py          # Manages SafariDriver session
│   ├── extractor.py                # Scrape dispatcher
│   ├── extractor_helpers.py        # Routes to ticket/POI logic
│   ├── tab_nav.py                  # Navigates between POI tabs
│   └── tab_ticket_scrapers/
│       ├── ticket_page.py          # Scrapes raw correction fields from tickets
│       ├── gemini_tab.py           # Placeholder for Gemini tab fields
│       ├── edits_tab.py            # Placeholder
│       ├── raps_tab.py             # Placeholder
│       ├── todos_tab.py            # Placeholder
│       └── versions_tab.py         # Placeholder
│
├── tests/                          # For unit or integration tests (TBD)
├── utils/                          # Future helper libraries/utilities
└── validator/                      # Validation or postprocessing modules (TBD)
```

---

## Config File Structure

* CSV with 564+ rows
* Column blocks repeat in groups of 3:

  * Column 1: Field name
  * Column 2: Checkbox (✓, x, 1, true)
  * Column 3: Optional column label (unused)
* One column for IDs: MUIDs, Place IDs, or Ticket IDs (typically only one type is populated per run)

---

## Execution Flow

1. **Launch**: Run `python3 run.py`
2. **Config Load**: `load_config()` identifies the active ID column and loads all rows for field requests.
3. **Manual Login Pause**: Optional manual `input()` pause allows Apple Connect login.
4. **Scraping**:

   * Ticket IDs → go to `/tickets/kittyhawk-beta/<id>`
   * MUIDs/Place IDs → go to `/p/release/<id>`
5. **Tab/Field Mapping**:

   * Ticket pages use `ticket_page.py`
   * POI pages route to Gemini, Versions, Todos, etc. via tab scrapers
6. **Output**: Writes results into `Output_Data/` with a timestamped filename

---

## Development Notes

* WebDriverWait guards are used to account for slow redirects and account logins.
* Scrapers are modular and can be extended field-by-field.
* All requested fields are global — they are not tied to the same row as an ID.

---

## Adding New Fields

1. Inspect the element via browser DevTools.
2. Copy a unique XPath for the element or use CSS Selectors.
3. Create a `get_<fieldname>()` function inside the appropriate scraper file. Should ideally match up with the attribute
    on the csv file exactly for clear intuition and readability.
4. Add a line in `scrape()` like:

   ```python
   if "Field Name" in requested_fields:
       result["Field Name"] = get_field_name(driver)
   ```

---

## Future Improvements

* Further XPATH and CSS testing needed to determine reliability. Will likely reference AnalysisAuto
* Retry on failed tickets
* UI-based checkbox field selector
* Pretty up results.csv file into more intuitive layout
* Get the driver set up for Chrome browsers as well

---

## Maintainer Notes

* Ticket page loading time can vary; sleep(10) is used for reliability
* Make sure to export config from Quip with headers starting at row 9
