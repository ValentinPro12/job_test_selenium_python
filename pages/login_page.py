from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.REGISTRATION_LINKS

    """
    Локаторый для страници логин
    """
    USERNAME = ('xpath', '//input[@id="user_nickname"]')
    PASSWORD = ('xpath', '//input[@name="user_password"]')
    REG_INPUT = ('xpath', '//input[@type="submit"]')

    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD)).send_keys(password)

    def click_reg_input(self):
        self.wait.until(EC.element_to_be_clickable(self.REG_INPUT)).click()
