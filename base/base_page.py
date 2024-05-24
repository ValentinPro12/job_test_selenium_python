import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.http_methods import Http_methods
from helpers import expect_equal

"""
базовый класс для всех старниц 
"""


class BasePage:
    notifications_text = ('xpath', '//td[@class="notifications-text-td"]')

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

    def check_usr_status(self):
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        print(self.PAGE_URL)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code, actual_value_url=self.PAGE_URL,
                     expected_value=200, url=current_url)

    def new_fanc(self):
        do = 1111
        v= 111
