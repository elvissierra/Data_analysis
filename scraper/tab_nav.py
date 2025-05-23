from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


COLUMN_TO_TAB = {
    "Place Details tab": "Gemini",      # default landing tab
    "Versions tab": "Versions",
    "RAPs tab": "RAPs",
    "Edits tab": "Edits",
    "Todos Tab": "Todos"
}


def click_tab(driver, tab, timeout=10):
    """
    Clicks a tab on the POI page by its visible text (e.g., "Todos", "Versions", etc.).
    Waits for a visible page change to confirm navigation.
    
    Args:
        driver: Selenium WebDriver instance
        tab_label (str): The visible label of the tab to click
        timeout (int): Seconds to wait for page load after click

    Returns:
        bool: True if the tab was clicked and content appeared, False otherwise
    """
    try:
        tab_label = driver.find_element(
            By.XPATH, f"//a[contains(@href, '/p/release/') and normalize-space(text())='{tab}']"
        )
        tab_label.click()
        print(f"Clicked '{tab}' tab")

        # Wait for content to change (can customize by tab if needed)
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//body"))  # Placeholder, refine per tab
        )
        return True

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Could not click tab '{tab}': {e}")
        return False


