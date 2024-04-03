import os

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    PAGE_URL = Links.CONFIG_MAIN_LINK
    MAIN_TITLE = f'{os.getenv("ENVIRONMENT")} \\ Настройки \\ Общие настройки1'

    link_to_home = ('xpath', '//a[@href="/development/testing/sc240314_0000_testing_prohorov_2920/SiteMap.php"]')
    breadcrumb_title = ('xpath', '//span[@id="breadcrumb_title"]')
    notifications = ('xpath', '//td[@class="notifications-text-td"]')

    def check(self):
        print('MainPage')
        super().check_usr_status()
        self.check_text()

    def check_text(self):
        breadcrumb_text = self.wait.until(EC.presence_of_element_located(self.breadcrumb_title)).text
        assert self.MAIN_TITLE == breadcrumb_text, (f"Название '{breadcrumb_text}' "
                                                    f"не соответствует ожидаемому заголовку '{self.MAIN_TITLE}'")
        self.wait.until(EC.element_to_be_clickable(self.link_to_home)).click()

