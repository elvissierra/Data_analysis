from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import time
import pandas as pd
import csv
import os

BASE_ADDRESS_KITTY_HAWK = "https://apollo.geo.apple.com/tickets/kittyhawk-sig/"
TODOS = "/todos"
output = "output.csv"
TIMEOUT = 30


def setup_driver():
    driver = webdriver.Safari()
    return driver


def open_kitty_hawk_todo(ticket_id, driver):
    driver.get(BASE_ADDRESS_KITTY_HAWK + ticket_id)
    time.sleep(40)


def open_automation_todo(ticket_id, driver):
    driver.get(BASE_ADDRESS_KITTY_HAWK + ticket_id + TODOS)
    time.sleep(40)


def get_name_suggestion(driver):
    row = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//tr[@class='base-edit-correction']")
        )
    )
    data_copyable = row.find_element(By.XPATH, ".//div[@data-copyable]")
    already_correct_suggestion = data_copyable.find_element(By.XPATH, ".//span").text
    cleaned_suggestion = already_correct_suggestion.strip()
    return cleaned_suggestion


def get_url_in_poi(driver):
    """Returns URL from POI"""
    try:
        url_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//div[contains(@class,'col-value')]//a[@data-copyable])[1]",
                )
            )
        )
        return url_el.get_attribute("href").strip()
    except TimeoutException:
        return None


def get_url_suggested(driver):
    """Returns suggested URL"""
    try:
        url_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//div[contains(@class,'col-value')]//a[@data-copyable])[2]",
                )
            )
        )

        return url_el.get_attribute("href").strip()
    except Exception:
        return None


def get_hours_listing_url(driver):
    """Hours listing Url"""
    try:
        xpath = (
            "//div[@title='Hours Listing']"
            "/following-sibling::div"
            "//a[@data-copyable]"
        )
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return elem.get_attribute("href").strip()
    except Exception:
        return None


def write_ticket_to_csv(
    ticket_id,
    name,
    url,
    url_suggested,
    hours_listing,
    file_path=output,
):
    df = pd.DataFrame(
        [[ticket_id, name, url, url_suggested, hours_listing]],
        columns=[
            "Ticket ID",
            "Name",
            "URL",
            "URL Suggested",
            "Hours_Listing_URL",
        ],
    )
    df.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)


def main():
    driver = setup_driver()
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()

    for x in range(len(df)):
        ticket_id = df["Ticket ID"].iloc[x]
        # if "automation" in ticket_id:
        #    print(f"Automation found in: {ticket_id}")
        # open_automation_todo(ticket_id, driver)
        # name_suggestion = get_name_suggestion(driver)
        # url = get_url_in_poi(driver)
        # url_suggested = get_url_suggested(driver)
        # write_ticket_to_csv(
        #    ticket_id,
        #    name_suggestion,
        #    url,
        #    url_suggested,
        # )
        # print(ticket_id)
        # print(name_suggestion)
        # print(url)
        # print(url_suggested)

        # else:
        # print(f"No automation in: {ticket_id}")
        open_kitty_hawk_todo(ticket_id, driver)
        name_suggestion = get_name_suggestion(driver)
        url = get_url_in_poi(driver)
        url_suggested = get_url_suggested(driver)
        hours_listing_url = get_hours_listing_url(driver)
        write_ticket_to_csv(
            ticket_id,
            name_suggestion,
            url,
            url_suggested,
            hours_listing_url,
        )
        print(
            f"{ticket_id} → "
            f"Name: {name_suggestion} | "
            # f"Closures: {closures} | "
            f"URL: {url} | "
            # f"Address: {address} | "
            # f"Geocode: {geocode} | "
            # f"Phone: {phone} | "
            # f"Hours: {all_year_round_hours} | "
            # f"Category: {modern_category}"
            f"URL: {url_suggested} | "
            f"URL: {hours_listing_url} | "
        )

    driver.quit()


if __name__ == "__main__":
    main()


"""
def get_address_suggestion(driver):
    address_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='ndm-address_address-line']")
        )
    )
    address = address_element.find_element(By.XPATH, ".//span").text
    cleaned_address = address.strip()
    return cleaned_address

def get_phone_in_poi(driver):
    phone_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@title='Number']"))
    )
    copyable = phone_element.find_element(
        By.XPATH, "following-sibling::div//div[@data-copyable]"
    )
    return copyable.text.strip()


def get_phone_suggested(driver):
    suggested_phone_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "(//div[@title='Number']/following-sibling::div//div[@data-copyable])[2]",
            )
        )
    )
    return suggested_phone_element.text.strip()

def get_hours_listing(driver):
    try:
        url_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//div[contains(@class,'col-value')]//a[@data-copyable])[3]",
                )
            )
        )
        return url_el.get_attribute("href").strip()
    except Exception:
        return None
"""
