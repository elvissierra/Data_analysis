from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Deprecated. Can still use these functions in proper tab/page scraper categories however. Delete at later date.


def get_name_suggestion(driver):
    row = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[contains(@class, 'base-edit-correction')]")
        )
    )
    data_copyable = row.find_element(By.XPATH, ".//div[@data-copyable]")
    return data_copyable.find_element(By.XPATH, ".//span").text.strip()


def get_address_suggestion(driver):
    address_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'ndm-address_address-line')]")
        )
    )
    return address_element.find_element(By.XPATH, ".//span").text.strip()


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
