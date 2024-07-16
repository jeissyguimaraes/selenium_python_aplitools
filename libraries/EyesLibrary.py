import os
import yaml
from applitools.selenium import Eyes, Target, BatchInfo
from selenium.webdriver.common.by import By

class EyesLibrary:
    def __init__(self):
        self.eyes = Eyes()
        self.load_config()

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'applitools_config.yaml')
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        self.eyes.api_key = config['api_key']
        self.eyes.server_url = config['server_url']
        self.batch = BatchInfo(config['app_name'])

    def open_eyes(self, driver, app_name, test_name):
        self.eyes.open(driver, app_name, test_name)

    def check_window_with_ignore(self, driver, css_selector):
        target = Target.window().ignore(By.CSS_SELECTOR, css_selector)
        self.eyes.check("Window with Ignore Region", target)

    def close_eyes(self):
        self.eyes.close(False)
