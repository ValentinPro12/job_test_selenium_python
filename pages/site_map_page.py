import requests

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from base.http_methods import Http_methods
from helpers import expect_equal


class SiteMapPage(BasePage):
    PAGE_URL = Links.SITE_MAP_LINK

    LINK_SITEMAP_STAT_COMMON = ('xpath', '//a[@id="link_sitemap_stat_common"]')

    def click_link(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_STAT_COMMON)).click()
        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_STAT_COMMON)).click()
        result = Http_methods.get(self.PAGE_URL)
        expect_equal(check_name="Код ответа сервера", actual_value=result.status_code,
                     expected_value=200)

