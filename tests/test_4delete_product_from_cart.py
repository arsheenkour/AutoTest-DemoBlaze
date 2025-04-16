import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

@pytest.fixture(scope="function")
def driver():
    chrome_service = Service("C:/selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com")
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot(f"screenshots/{name}.png")

def test_delete_product(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # Add product
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))).click()
        time.sleep(1)
        driver.switch_to.alert.accept()

        # Go to cart
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)

        # Delete item
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete"))).click()
        time.sleep(2)

        take_screenshot(driver, "delete_product")

    except Exception as e:
        take_screenshot(driver, "delete_failed")
        pytest.fail(f"Delete test failed: {e}")
