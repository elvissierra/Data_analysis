from selenium import webdriver

def start_driver():
    print("Launching Safari browser...")

    try:
        driver = webdriver.Safari()
        driver.set_window_size(1200, 800)
        return driver
    except Exception as e:
        print(f"Failed to launch Safari: {e}")
        return None