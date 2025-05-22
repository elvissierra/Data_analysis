from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import pandas as pd
import csv

BASE_ADDRESS_KITTY_HAWK = "https://apollo.geo.apple.com/tickets/kittyhawk-sig/"
TODOS = "/todos"
output = 'output.csv'

def setup_driver():
    driver = webdriver.Safari()
    return driver

def open_kitty_hawk_todo(id, driver):
    driver.get(BASE_ADDRESS_KITTY_HAWK + id)
    time.sleep(40)

def open_automation_todo(id, driver):
    driver.get(BASE_ADDRESS_KITTY_HAWK + id + TODOS)
    time.sleep(40)

def get_name_suggestion(driver):
    row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@class='base-edit-correction']"))
        )
        
    # Find the div with the 'data-copyable' attribute inside this row
    data_copyable = row.find_element(By.XPATH, ".//div[@data-copyable]")

    # Get the text inside the <span> within the data-copyable div
    already_correct_suggestion = data_copyable.find_element(By.XPATH, ".//span").text
    
    cleaned_suggestion = already_correct_suggestion.strip() 
    return cleaned_suggestion

def write_suggestions_to_csv(id, name, file_path=output):
    # Create a DataFrame with one row, suggestion in second column
    df = pd.DataFrame([[id, name]])
    df.to_csv(file_path, mode='a', header=False, index=False)
    
def get_address_suggestion(driver):
    address_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='ndm-address_address-line']"))
    )
    address = address_element.find_element(By.XPATH, ".//span").text
    cleaned_address = address.strip()
    return cleaned_address

# Elvis
def get_phone_in_poi(driver):
    """ Scrape phone number from the POI section of the web page using driver """
    phone_xpath = (
        "//div[@title='Number']"
        "/following-sibling::div"         # col-value container
        "//div[@data-copyable]"           # the actual number holder
    )
    elem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, phone_xpath))
    )
    return elem.text.strip().strip('"')

def get_phone_suggestion(driver):
    # TODO (Elvis): Scrape suggested phone number from the web page using driver
    pass

def get_url_in_poi(driver):
    # TODO (Elvis): Scrape URL from the POI section of the web page using driver
    pass

def get_url_suggestion(driver):
    # TODO (Elvis): Scrape suggested URL from the web page using driver
    pass


# William
def get_address_in_poi(driver):
    # TODO (William): Scrape address from the POI section of the web page using driver
    pass

def get_closure_in_poi(driver):
    # TODO (William): Scrape closure status from the POI section of the web page using driver
    pass

def get_closure_suggestion(driver):
    # TODO (William): Scrape suggested closure status from the web page using driver
    pass

def get_country_code(driver):
    # TODO (William): Scrape country code from the web page or metadata using driver
    pass

def get_geocode_in_poi(driver):
    # TODO (William): Scrape geocode from the POI section of the web page using driver
    pass


# Alex
def get_geocode_suggestion(driver):
    # TODO (Alex): Scrape suggested geocode (lat/lng) from the web page using driver
    pass

def get_hour_in_poi(driver):
    # TODO (Alex): Scrape business hours from the POI section of the web page using driver
    pass

def get_hour_suggestion(driver):
    # TODO (Alex): Scrape suggested business hours from the web page using driver
    pass

def get_modern_category_in_poi(driver):
    # TODO (Alex): Scrape modern category from the POI section of the web page using driver
    pass

def get_modern_category_suggestion(driver):
    # TODO (Alex): Scrape suggested modern category from the web page using driver
    pass

def get_name_in_poi(driver):
    # TODO (Alex): Scrape name from the POI section of the web page using driver
    pass




def main():
    driver = setup_driver()
    
    df = pd.read_csv('data.csv')
    df.columns = df.columns.str.strip()  # 🧼 Clean up column names
    
    for x in range(len(df)):
        id = df['Ticket ID'].iloc[x]
        if "automation" in id:
            print(f"Automation found in: {id}")
            open_automation_todo(id, driver)
            #name_suggestion = get_name_suggestion(driver)
            #print(id, name_suggestion)
            #write_suggestions_to_csv(id, name_suggestion)
            #address = get_address_suggestion(driver)
            #print(address)
        else:
            print(f"No automation in: {id}")
            open_kitty_hawk_todo(id, driver)
            name_suggestion = get_name_suggestion(driver)
            print(name_suggestion)
            #write_suggestions_to_csv(id, name_suggestion)
            #address = get_address_suggestion(driver)
            #print(address)

    driver.quit()


if __name__ == '__main__':
    main()