from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

class BrowserManager:
    def __init__(self):
        self.driver = None

    def start_browser(self, headless=False):
        options = Options()
        if headless:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=ChromeService(), options=options)
        self.driver.maximize_window()
        return self.driver

    def stop_browser(self):
        if self.driver:
            self.driver.quit()
