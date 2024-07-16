from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage
from pages.selectors import LoginPageSelectors

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, LoginPageSelectors.USERNAME_INPUT)
        self.password_input = (By.ID, LoginPageSelectors.PASSWORD_INPUT)
        self.login_button = (By.ID, LoginPageSelectors.LOGIN_BUTTON)

    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.wait_for_element(self.username_input).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.password_input).send_keys(password)

    def click_login_button(self):
        self.wait_for_element(self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
