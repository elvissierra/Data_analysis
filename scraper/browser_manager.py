# browser_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

    # let webdriver_manager download (if needed) & return the correct binary path
    service = Service(ChromeDriverManager().install())

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Failed to launch Chrome: {e}")
        return None
