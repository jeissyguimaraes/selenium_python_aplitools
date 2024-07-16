from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage
from pages.selectors import InventoryPageSelectors

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_container = (By.CLASS_NAME, InventoryPageSelectors.INVENTORY_CONTAINER)

    def is_loaded(self):
        return self.wait_for_element(self.inventory_container).is_displayed()
