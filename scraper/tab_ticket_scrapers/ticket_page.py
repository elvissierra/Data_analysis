from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape(driver, requested_fields):
    result = {}

    if "Corrections col - Address - Raw Address" in requested_fields:
        result["Corrections col - Address - Raw Address"] = get_address_corrections_col(
            driver
        )

    return result


""" ===Field Scraping Logic=== 

#Below is a template for any attribute under any tab or page. Just experiment with XPATH or CSS selectors 
until you're able to successfully pull the data across multiple tickets/records. 

def get_field_x(driver):
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "<your_xpath_here>"))
        )
        return elem.text.strip()
    except Exception as e:
        print("Error scraping 'Field X':", e)
        return "Error"

"""


def get_address_corrections_col(driver):
    try:
        # Wait up to 10 seconds for the address span to appear
        address_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@title='Raw Address']/following-sibling::div//div[contains(@class, 'ndm-address_address-line')]//span",
                )
            )
        )
        return address_elem.text.strip()

    except Exception as e:
        print("Error scraping 'Corrections col - Address - Raw Address':", e)
        return "Error"
