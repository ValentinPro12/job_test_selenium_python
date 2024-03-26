import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
базовый класс для всех старниц 
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self) -> None:
        """
        Открытие страници
        """
        with allure.step(f'Открытие {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)

    def is_opened(self) -> None:
        """
        Проверка что страница открыта
        """
        with allure.step(f'Страница {self.PAGE_URL} открылась'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))
