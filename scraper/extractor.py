from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://apollo-staging.geo.apple.com/tickets/kittyhawk-beta/"
TODOS_PATH = "/todos"


def scrape_ticket_data(driver, muid, row_config=None):
    print(f"Navigating to POI for MUID: {muid}")

    url = f"{BASE_URL}{muid}{TODOS_PATH}"

    try:
        driver.get(url)
        sleep(5)

        name = get_name_suggestion(driver)
        address = get_address_suggestion(driver)

        return {
            "MUIDs": muid,
            "Suggested Name": name,
            "Suggested Address": address,
            "Validation Notes": "Stubbed: No comparison logic yet",
        }

    except Exception as e:
        print(f"Failed to load or scrape MUID {muid}: {e}")
        return {
            "MUIDs": muid,
            "Suggested Name": "",
            "Suggested Address": "",
            "Validation Notes": f"Error: {str(e)}",
        }


def get_name_suggestion(driver):
    try:
        row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//tr[@class='base-edit-correction']")
            )
        )
        data_copyable = row.find_element(By.XPATH, ".//div[@data-copyable]")
        suggestion = data_copyable.find_element(By.XPATH, ".//span").text.strip()
        return suggestion
    except Exception as e:
        print(f"Could not extract name suggestion: {e}")
        return ""


def get_name_in_poi(driver):
    # """Scrape current POI name from the POI section."""
    pass


def get_address_suggestion(driver):
    try:
        address_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='ndm-address_address-line']")
            )
        )
        address = address_element.find_element(By.XPATH, ".//span").text.strip()
        return address
    except Exception as e:
        print(f"Could not extract address suggestion: {e}")
        return ""


def get_address_in_poi(driver):
    # """Scrape address from the POI section of the web page using driver."""
    pass


def get_closure_in_poi(driver):
    # """Scrape closure status from the POI section of the web page using driver."""
    pass


def get_closure_suggestion(driver):
    # """Scrape suggested closure status from the ToDo section of the web page using driver."""
    pass


def get_country_code(driver):
    # """Scrape country code from the POI or metadata."""
    pass


def get_geocode_in_poi(driver):
    # """Scrape geocode from the POI section (lat/lng)."""
    pass


def get_geocode_suggestion(driver):
    # """Scrape suggested geocode (lat/lng) from the ToDo section."""
    pass


def get_hour_in_poi(driver):
    # """Scrape hours from the POI section of the web page."""
    pass


def get_hour_suggestion(driver):
    # """Scrape suggested hours from the ToDo section of the web page."""
    pass


def get_modern_category_in_poi(driver):
    # """Scrape modern category from the POI section."""
    pass


def get_modern_category_suggestion(driver):
    # """Scrape suggested modern category from the ToDo section."""
    pass


def get_phone_in_poi(driver):
    # """Scrape phone number from the POI section."""
    pass


def get_phone_suggestion(driver):
    # """Scrape suggested phone number from the ToDo section."""
    pass


def get_url_in_poi(driver):
    # """Scrape website URL from the POI section."""
    pass


def get_url_suggestion(driver):
    # """Scrape suggested website URL from the ToDo section."""
    pass
