from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

class BaseTest:
    def setup(self):
        chrome_driver_path = "C:/selenium/chromedriver.exe"
        chrome_service = Service(chrome_driver_path)

        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com")
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

    def take_screenshot(self, name):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")
