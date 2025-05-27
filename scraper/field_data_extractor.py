from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Deprecated. Can still use these functions in proper tab/page scraper categories however. Delete at later date.


def get_name_suggestion(driver):
    """
    Scrapes customer name suggestion.
    """
    try:
        base_edit_corrections = driver.find_elements(
            By.CLASS_NAME, "base-edit-correction"
        )
        name = base_edit_corrections[0]
        name_cleaned = name.find_element(
            By.CSS_SELECTOR, "[data-copyable] span"
        ).text.strip()
        return name_cleaned
    except Exception as e:
        return None


def get_address_suggestion(driver):
    """
    Scrapes customer address suggestion.
    """
    try:
        base_edit_corrections = driver.find_elements(
            By.CLASS_NAME, "base-edit-correction"
        )
        address = base_edit_corrections[2]
        address_name_cleaned = address.find_element(
            By.CLASS_NAME, "ndm-address_address-line"
        ).text.strip()
        return address_name_cleaned
    except Exception as e:
        return None


def get_name_suggestion(driver):
    """
    Scrapes customer name suggestion.
    """
    try:
        base_edit_corrections = driver.find_elements(
            By.CLASS_NAME, "base-edit-correction"
        )
        name = base_edit_corrections[0]
        name_cleaned = name.find_element(
            By.CSS_SELECTOR, "[data-copyable] span"
        ).text.strip()
        return name_cleaned
    except Exception as e:
        return None


def get_name_in_poi(driver):
    """Scrape current POI name from the POI section."""
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
    """
    Scrapes addresses from POI address sections.
    """
    try:
        selector = (By.CSS_SELECTOR, 'div[data-id="0"] .ndm-address_address-line span')
        element = driver.find_element(*selector)
        return element.get_attribute("innerText").strip()
    except Exception as e:
        print(f"Error extracting raw address: {e}")
        return None


def get_closure_in_poi(driver):
    """
    Scrapes the closure status from the POI section.
    """

    try:
        selector = (
            By.CSS_SELECTOR,
            "div.base-edit-list.base-ranked-edit-list.array-edit-state-ranked-edit-list span.text-placeholder",
        )
        element = driver.find_element(*selector)
        return element.text.strip()
    except Exception as e:
        print(f"Error extracting closure status: {e}")
        return None


def get_closure_suggestion(driver):
    """
    Scrape suggested closure status from the ToDo section of the web page using driver.
    """
    pass


def get_country_code(driver):
    """
    Scrapes country code in POI.
    """
    try:
        selector = (
            By.CSS_SELECTOR,
            'div[data-id="country_code"] .base-edit-item__content span',
        )
        element = driver.find_element(*selector)
        return element.text.strip()
    except Exception as e:
        return None


def get_geocode_in_poi(driver):
    """
    Scrape geocode from the POI section (lat/lng).
    """
    pass


def get_geocode_suggestion(driver):
    try:
        selector = (
            By.CSS_SELECTOR,
            "tr.base-edit-correction td.text-break div.point a",
        )
        geocode_element = driver.find_element(*selector)
        geocode_text = geocode_element.text.strip()
        return geocode_text
    except Exception as e:
        return None


def get_hour_in_poi(driver):
    """Scrape hours from the POI section of the web page."""
    pass


def get_hour_suggestion(driver):
    """Scrape suggested hours from the ToDo section of the web page."""
    pass


def get_modern_category_in_poi(driver):
    """Scrape modern category from the POI section."""
    pass


def get_modern_category_suggestion(driver):
    """Scrape suggested modern category from the ToDo section."""
    pass


def get_phone_in_poi(driver):
    """Scrape phone number from the POI section."""
    pass


def get_phone_suggestion(driver):
    """Scrape suggested phone number from the ToDo section."""
    pass


def get_url_in_poi(driver):
    """Scrape website URL from the POI section."""
    pass


def get_url_suggestion(driver):
    """Scrape suggested website URL from the ToDo section."""
    pass
