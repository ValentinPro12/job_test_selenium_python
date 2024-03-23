import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.http_methods import Http_methods
from helpers import expect_equal


class SiteMapPage(BasePage):
    PAGE_URL = Links.SITE_MAP_LINK

    LINK_SITEMAP_COMMON = ('xpath', '//a[@id="link_sitemap_stat_common"]')
    LINK_SITEMAP_COMMONS = ('xpath', '//a[@id="link_sitemap_stat_contacts"]')
    LINK_SITEMAP_AGENTS = ('xpath', '//a[@id="link_sitemap_stat_agents"]')
    LINK_SITEMAP_CALLS = ('xpath', '//a[@id="link_sitemap_stat_calls"]')
    LINK_SITEMAP_FINALCATEGORIES = ('xpath', '//a[@id="link_sitemap_stat_finalcategories"]')
    LINK_SITEMAP_MESSAGES = ('xpath', '//a[@id="link_sitemap_stat_messages"]')
    LINK_SITEMAP_TRANSFERS = ('xpath', '//a[@id="link_sitemap_stat_transfers"]')
    LINK_SITEMAP_EXTENDED = ('xpath', '//a[@id="link_sitemap_stat_extended"]')
    LINK_SITEMAP_XTERNAL = ('xpath', '//a[@id="link_sitemap_stat_external"]')
    LINK_SITEMAP_VOTING = ('xpath', '//a[@id="link_sitemap_stat_voting"]')
    LINK_SITEMAP_AGENTSRATING = ('xpath', '//a[@id="link_sitemap_stat_agentsrating"]')
    LINK_SITEMAP_OBJECTS = ('xpath', '//a[@id="link_sitemap_stat_objects"]')
    LINK_SITEMAP_CHATS = ('xpath', '//a[@id="link_sitemap_stat_chats"]')
    LINK_SITEMAP_ATTACHMENTS = ('xpath', '//a[@id="link_sitemap_stat_attachments"]')
    LINK_HOME = ('xpath', '//a[@href="/development/testing/sc240314_0000_testing_prohorov_2920/SiteMap.php"]')
    BREADCRUMB_TITLE = ('xpath', '//span[@id="breadcrumb_title"]')

    def click_link(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_COMMON)).click()
        element = self.wait.until(EC.presence_of_element_located(self.BREADCRUMB_TITLE))

        # Получение текста элемента
        text = element.text
        print(text)

        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_COMMONS)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_AGENTS)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_CALLS)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_FINALCATEGORIES)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_MESSAGES)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_TRANSFERS)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_EXTENDED)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_XTERNAL)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_VOTING)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_AGENTSRATING)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_OBJECTS)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_CHATS)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable(self.LINK_SITEMAP_ATTACHMENTS)).click()
        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.LINK_HOME)).click()
        time.sleep(2)
