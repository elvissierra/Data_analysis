from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape(driver, requested_fields):
    result = {}
    print("REQUESTED FIELDS IN GEM TAB", requested_fields)

    if "Corrections col - Address - Raw Address" in requested_fields:
        result["Corrections col - Address - Raw Address"] = get_formatted_address(driver)
    if "Carto Score" in requested_fields:
        result["Carto Score"] = get_carto_score(driver)
    print("SHOULD SEE THIS NO MATTER WHAT", result)


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



def get_formatted_address(driver):
    try:
        
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='address-formatted']"))
        )
        return element.text.strip()
    except Exception as e:
        print(f"Error extracting formatted address: {e}")
        return ""




from time import sleep

def get_carto_score(driver):
    try:
        print("Finding render sweetspot...")
        sleep(15)  
        print("done waiting.")

     
        value_div = driver.find_element(
            By.CSS_SELECTOR,
            'div[title="Carto Score"] + div.col-value'
        )


        print("Attempting to find <span> inside value div...")
        span_elem = value_div.find_element(By.CSS_SELECTOR, "span")
        js_text = driver.execute_script("return arguments[0].textContent;", span_elem).strip()

  

        # Prefer JS-based textContent to bypass Vue weirdness
        return js_text if js_text else "Empty Carto Score (CSS)"

    except Exception as e:
        print("❌ STEP X: Exception during Carto Score scrape")
        import traceback
        traceback.print_exc()
        return "Unable to find Carto Score"


"""
def get_carto_score(driver):
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@title='Carto Score']")
            )
        )

        score_elem = driver.find_element(
            By.XPATH,
            "//div[@title='Carto Score']/following-sibling::div[contains(@class, 'col-value text-break col-10')]/span"
        )

        # Use JS to extract raw textContent in case .text fails
        score = driver.execute_script("return arguments[0].textContent;", score_elem).strip()

        return score if score else "Empty Carto Score (via JS)"

    except Exception as e:
        print(f"❌ Error extracting Carto Score: {e}")
        return "Unable to find Carto Score"

"""





def get_muid(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='muid']"))
        )
        return element.text.strip()
    except Exception as e:
        print(f"Error extracting MUID: {e}")
        return ""


def get_created_timestamp(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='created-timestamp']"))
        )
        return element.text.strip()
    except Exception as e:
        print(f"Error extracting Created timestamp: {e}")
        return ""
