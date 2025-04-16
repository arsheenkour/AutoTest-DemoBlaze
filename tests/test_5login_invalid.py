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

def test_login_success(driver):
    wait = WebDriverWait(driver, 10)

    try:
        # Click login button
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        time.sleep(1)

        # Enter credentials
        wait.until(EC.presence_of_element_located((By.ID, "loginusername"))).send_keys("arsh")
        driver.find_element(By.ID, "loginpassword").send_keys("ak1234")
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        # Wait to ensure user is logged in
        time.sleep(3)
        take_screenshot(driver, "login_success")

    except Exception as e:
        take_screenshot(driver, "login_failed")
        pytest.fail(f"Login test failed: {e}")
