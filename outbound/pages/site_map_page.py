import time
import os

import allure
from dotenv import load_dotenv
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

from outbound.pages.config.main_page import MainPage

load_dotenv()


class SiteMapPage(BasePage):
    """
       Класс SiteMapPage, отвечает за то что
       бы полностью пройти все пункты меню на указанной странице.
       имеет  методы click_link
       информирует о status_code, current_url, element_text
       """
    PAGE_URL = Links.SITE_MAP_LINK

    MAIN_TITLE = f'{os.getenv("ENVIRONMENT")} \\ Карта проекта'

    link_to_home = ('xpath', '//a[@href="/development/testing/sc240314_0000_testing_prohorov_2920/SiteMap.php"]')
    breadcrumb_title = ('xpath', '//span[@id="breadcrumb_title"]')
    link_sitemap_config_main = ('xpath', '//a[@id="link_sitemap_config_main"]')
    link_sitemap_config_survey = ('xpath', '//a[@id="link_sitemap_config_survey"]')
    notifications = ('xpath', '//td[@class="notifications-text-td"]')
    text = 'Добро пожаловать в проект "sc240314_0000_testing_prohorov_2920".'

    def cek_text(self):
        breadcrumb_text = self.wait.until(EC.presence_of_element_located(self.breadcrumb_title)).text
        notifications_text = self.wait.until(EC.presence_of_element_located(self.notifications)).text
        assert self.MAIN_TITLE == breadcrumb_text, (f"Название '{breadcrumb_text}' не соответствует ожидаемому "
                                                    f"заголовку '{self.MAIN_TITLE}'")
        assert self.text == notifications_text, (f"Название '{self.text}' "
                                                 f"не соответствует ожидаемому заголовку '{self.text}'")

    def click_settings_link(self):
        self.wait.until(EC.element_to_be_clickable(self.link_sitemap_config_main)).click()

    def click_sitemap_config_survey(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.link_sitemap_config_survey)).click()
