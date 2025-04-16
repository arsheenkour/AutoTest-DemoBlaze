import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Fixture to set up and tear down browser
@pytest.fixture(scope="function")
def driver():
    chrome_service = Service("C:/selenium/chromedriver.exe") 
    driver = webdriver.Chrome(service=chrome_service)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com")
    yield driver
    driver.quit()

# Screenshot helper
def take_screenshot(driver, name):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot(f"screenshots/{name}.png")

# Test: Add a single product to cart
def test_add_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # Click on product
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))).click()

        # Add to cart
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))).click()
        time.sleep(2)

        # Accept alert
        driver.switch_to.alert.accept()

        # Go to cart
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)

        # Validate item present
        product_present = wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='Samsung galaxy s6']")))
        assert product_present is not None, "Product not found in cart"

        take_screenshot(driver, "add_to_cart_success")

    except Exception as e:
        take_screenshot(driver, "add_to_cart_failed")
        pytest.fail(f"Add to Cart test failed: {e}")
