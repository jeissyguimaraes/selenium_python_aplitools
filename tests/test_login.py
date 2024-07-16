import sys
import os
import json

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from libraries.BrowserManager import BrowserManager
from libraries.EyesLibrary import EyesLibrary
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Carregar dados de teste
with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json'), 'r') as file:
    data = json.load(file)

class TestLogin:
    def setup_method(self):
        # Initialize browser manager and Applitools Eyes
        self.browser_manager = BrowserManager()
        self.eyes_library = EyesLibrary()
        
        # Start the browser
        self.driver = self.browser_manager.start_browser()

    def teardown_method(self):
        # Stop the browser
        self.browser_manager.stop_browser()

    def initialize_eyes(self, app_name, test_name):
        self.eyes_library.open_eyes(self.driver, app_name, test_name)

    def test_login_with_visual_test(self):
        # Initialize page objects
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)

        # Open the target URL and perform login
        login_page.open(data['url'])
        login_page.login(data['username'], data['password'])

        # Initialize Applitools Eyes for visual testing
        self.initialize_eyes(data['app_name'], data['test_name'])

        # Perform visual testing
        self.eyes_library.check_window_with_ignore(self.driver, data['ignore_selector'])
        self.eyes_library.close_eyes()
