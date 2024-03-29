import time
import os

import allure
from dotenv import load_dotenv
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from base.http_methods import Http_methods
from helpers import expect_equal

load_dotenv()


class SiteMapPage(BasePage):
    """
       Класс SiteMapPage, отвечает за то что
       бы полностью пройти все пункты меню на указанной странице.
       имеет  методы click_link
       информирует о status_code, current_url, element_text
       """
    PAGE_URL = Links.SITE_MAP_LINK
    print(PAGE_URL)

    LINKS_DICT = {

        'config_main': ('xpath', '//a[@id="link_sitemap_config_main"]'),

    }
    # MAIN_TITLE = os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Общие настройки',
    MAIN_TITLE=f'{os.getenv("ENVIRONMENT")} \\ Карта проекта'

    link_to_home = ('xpath', '//a[@href="/development/testing/sc240314_0000_testing_prohorov_2920/SiteMap.php"]')
    breadcrumb_title = ('xpath', '//span[@id="breadcrumb_title"]')
    notifications = ('xpath', '//td[@class="notifications-text-td"]')
    text = 'Добро пожаловать в проект "sc240314_0000_testing_prohorov_2920".'

    def cek_text(self):
        breadcrumb_text = self.wait.until(EC.presence_of_element_located(self.breadcrumb_title)).text
        # notifications_text = self.wait.until(EC.presence_of_element_located(self.notifications)).text
        assert self.MAIN_TITLE == breadcrumb_text, f"Название '{breadcrumb_text}' не соответствует ожидаемому заголовку '{self.MAIN_TITLE}'"
        # assert notifications_text == text, f"Название '{text}' не соответствует ожидаемому заголовку '{MAIN_TITLE}'"
