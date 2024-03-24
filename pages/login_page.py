from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    """
    Класс LoginPage для авторизации на ресерсе.
    имеет  методы enter_login, enter_password, click_reg_input
    """
    PAGE_URL = Links.REGISTRATION_LINKS

    """
    Локаторый для страници логин
    """
    USERNAME = ('xpath', '//input[@id="user_nickname"]')
    PASSWORD = ('xpath', '//input[@name="user_password"]')
    REG_INPUT = ('xpath', '//input[@type="submit"]')

    def enter_login(self, login: str):
        """
        Ввод логина

        :param login: логин
        """
        self.wait.until(EC.element_to_be_clickable(self.USERNAME)).send_keys(login)

    def enter_password(self, password: str):
        """
        Ввод логина
        :param password: пароль
        """
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD)).send_keys(password)

    def click_reg_input(self):
        """
        клик на кнопку регистрации
        """
        self.wait.until(EC.element_to_be_clickable(self.REG_INPUT)).click()
