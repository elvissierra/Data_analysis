import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def start_driver():
    print("Launching Chrome browser…")

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1200,800")
    chrome_options.add_argument(
        "--load-extension=/Users/nhtimac/Library/Application Support/"
        "Google/Chrome/Default/Extensions/"
        "bnmgcoghgdbfcnokmmjbabgjphmfnmgl/1.2.0_0"
    )

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path, log_path="/dev/null")

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        logging.error("Failed to launch ChromeDriver: %s", e)
        return None
