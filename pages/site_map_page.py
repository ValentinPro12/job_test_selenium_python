import requests

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.http_methods import Http_methods
from helpers import expect_equal


class SiteMapPage(BasePage):
    PAGE_URL = Links.SITE_MAP_LINK

    LINK_SITEMAP_STAT_COMMON = ('xpath', '//a[@id="link_sitemap_stat_common"]')
    LINK_SITEMAP_STAT_COMMONS = ('xpath', '//a[@id="link_sitemap_stat_contacts"]')
    LINK_HOME = ('xpath', '//a[@href="/development/testing/sc240314_0000_testing_prohorov_2920/SiteMap.php"]')
    # BREADCRUMB_TITLE =  ('xpath', '//td[@class="notifications-text-td"]')
    BREADCRUMB_TITLE =  ('xpath', '//span[@id="breadcrumb_title"]')

    # def click_link(self):
    #     self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_STAT_COMMON)).click()
    #     var = self.driver.current_url
    #     print(var)
    #     self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
    #     self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_STAT_COMMONS)).click()
    #     self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
    #
    #     result = Http_methods.get(self.PAGE_URL)
    #     # print(self.PAGE_URL)
    #     expect_equal(check_name="Код ответа сервера", actual_value=result.status_code,
    #                  expected_value=200)

    def click_link(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_STAT_COMMON)).click()
        element =  self.wait.until(EC.presence_of_element_located(self.BREADCRUMB_TITLE))

        # Получение текста элемента
        text = element.text
        print(text)


        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                         expected_value=200, url=current_url)
        # assert response.status_code == 200, f"Expected status code 200, but got {response.status_code} for URL {current_url}"

        # self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        # current_url = self.driver.current_url
        # response = Http_methods.get(current_url)
        # assert response.status_code == 200, \
        #     f"Expected status code 200, but got {response.status_code} for URL {current_url}"
        #
        # self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_STAT_COMMONS)).click()
        # current_url = self.driver.current_url
        # response = Http_methods.get(current_url)
        # assert response.status_code == 200, \
        #     f"Expected status code 200, but got {response.status_code} for URL {current_url}"
