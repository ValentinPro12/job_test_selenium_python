import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from base.http_methods import Http_methods
from helpers import expect_equal


class SiteMapPage(BasePage):
    """
       Класс SiteMapPage, отвечает за то что
       бы полностью пройти все пункты меню на указанной странице.
       имеет  методы click_link
       информирует о status_code, current_url, element_text
       """
    PAGE_URL = Links.SITE_MAP_LINK

    LINKS_DICT = {
        'common': ('xpath', '//a[@id="link_sitemap_stat_common"]'),
        'commons': ('xpath', '//a[@id="link_sitemap_stat_contacts"]'),
        'agents': ('xpath', '//a[@id="link_sitemap_stat_agents"]'),
        'calls': ('xpath', '//a[@id="link_sitemap_stat_calls"]'),
        'finalcategories': ('xpath', '//a[@id="link_sitemap_stat_finalcategories"]'),
        'messages': ('xpath', '//a[@id="link_sitemap_stat_messages"]'),
        'transfers': ('xpath', '//a[@id="link_sitemap_stat_transfers"]'),
        'extended': ('xpath', '//a[@id="link_sitemap_stat_extended"]'),
        'xternal': ('xpath', '//a[@id="link_sitemap_stat_external"]'),
        'voting': ('xpath', '//a[@id="link_sitemap_stat_voting"]'),
        'agentsrating': ('xpath', '//a[@id="link_sitemap_stat_agentsrating"]'),
        'objects': ('xpath', '//a[@id="link_sitemap_stat_objects"]'),
        'chats': ('xpath', '//a[@id="link_sitemap_stat_chats"]'),
        'attachments': ('xpath', '//a[@id="link_sitemap_stat_attachments"]'),

        'config_main': ('xpath', '//a[@id="link_sitemap_config_main"]'),
        'config_survey': ('xpath', '//a[@id="link_sitemap_config_survey"]'),
        'config_widgets': ('xpath', '//a[@id="link_sitemap_config_widgets"]'),
        'config_callprocessing': ('xpath', '//a[@id="link_sitemap_config_callprocessing"]'),
        'config_telephony': ('xpath', '//a[@id="link_sitemap_config_telephony"]'),
        'config_contactprocessing': ('xpath', '//a[@id="link_sitemap_config_contactprocessing"]'),
        'config_stat': ('xpath', '//a[@id="link_sitemap_config_stat"]'),
        'config_importdata': ('xpath', '//a[@id="link_sitemap_config_importdata"]'),
        'config_exportdata': ('xpath', '//a[@id="link_sitemap_config_exportdata"]'),
        'config_operator': ('xpath', '//a[@id="link_sitemap_config_operator"]'),
        'config_customer': ('xpath', '//a[@id="link_sitemap_config_customer"]'),
        'config_batchprocessing': ('xpath', '//a[@id="link_sitemap_config_batchprocessing"]'),
        'config_api': ('xpath', '//a[@id="link_sitemap_config_api"]'),
        'config_callsschedule': ('xpath', '//a[@id="link_sitemap_config_callsschedule"]'),
        'config_voting': ('xpath', '//a[@id="link_sitemap_config_voting"]'),
        'config_health': ('xpath', '//a[@id="link_sitemap_config_health"]'),
        'config_callbackwidget': ('xpath', '//a[@id="link_sitemap_config_callbackwidget"]'),
        'config_objecttype': ('xpath', '//a[@id="link_sitemap_config_objecttype"]'),
        'config_chats': ('xpath', '//a[@id="link_sitemap_config_chats"]'),

        'importdata_importdata': ('xpath', '//a[@id="link_sitemap_importdata_importdata"]'),
        'importdata_yes_button': ('xpath', '//button[@id="exitConfirmModalYesButton"]'),
        'importdata_editimportdata': ('xpath', '//a[@id="link_sitemap_importdata_editimportdata"]'),
        'importdata_adminimportdata': ('xpath', '//a[@id="link_sitemap_importdata_adminimportdata"]'),

        'exportdata_exportdata': ('xpath', '//a[@id="link_sitemap_exportdata_exportdata"]'),
        'exportdata_editexportdata': ('xpath', '//a[@id="link_sitemap_exportdata_editexportdata"]'),
        'edit_survey': ('xpath', '//a[@id="link_sitemap_edit_survey"]'),
        'edit_registries': ('xpath', '//a[@id="link_sitemap_edit_registries"]'),
        'edit_finalcategories': ('xpath', '//a[@id="link_sitemap_edit_finalcategories"]'),
        'edit_textcontent': ('xpath', '//a[@id="link_sitemap_edit_textcontent"]'),
        'edit_navigationnodes': ('xpath', '//a[@id="link_sitemap_edit_navigationnodes"]'),
        'edit_filestorage': ('xpath', '//a[@id="link_sitemap_edit_filestorage"]'),
        'edit_messages': ('xpath', '//a[@id="link_sitemap_edit_messages"]'),
        'edit_listtransfer': ('xpath', '//a[@id="link_sitemap_edit_listtransfer"]'),
        'edit_statuses': ('xpath', '//a[@id="link_sitemap_edit_statuses"]'),
        'edit_quotas': ('xpath', '//a[@id="link_sitemap_edit_quotas"]'),
        'edit_catalogs': ('xpath', '//a[@id="link_sitemap_edit_catalogs"]'),
        'edit_callsschedule': ('xpath', '//a[@id="link_sitemap_edit_callsschedule"]'),
        'module_knowledgenodes': ('xpath', '//a[@id="link_sitemap_module_knowledgenodes"]'),
        'monitoring_telephony': ('xpath', '//a[@id="link_sitemap_monitoring_telephony"]'),
        'monitoring_activity': ('xpath', '//a[@id="link_sitemap_monitoring_activity"]'),
        'monitoring_services': ('xpath', '//a[@id="link_sitemap_monitoring_services"]'),
        'monitoring_indicators': ('xpath', '//a[@id="link_sitemap_monitoring_indicators"]'),
        'monitoring_health': ('xpath', '//a[@id="link_sitemap_monitoring_health"]'),
        'admin_information': ('xpath', '//a[@id="link_sitemap_admin_information"]'),
        'admin_news': ('xpath', '//a[@id="link_sitemap_admin_news"]'),
        'admin_notifications': ('xpath', '//a[@id="link_sitemap_admin_notifications"]'),
        'admin_batchprocessing': ('xpath', '//a[@id="link_sitemap_admin_batchprocessing"]'),
        'admin_feedback': ('xpath', '//a[@id="link_sitemap_admin_feedback"]')
    }

    link_to_home = ('xpath', '//a[@href="/development/testing/sc240314_0000_testing_prohorov_2920/SiteMap.php"]')
    breadcrumb_title = ('xpath', '//span[@id="breadcrumb_title"]')

    def click_link(self, link_name: str):
        self.wait.until(EC.element_to_be_clickable(self.LINKS_DICT[link_name])).click()
        element = self.wait.until(EC.presence_of_element_located(self.breadcrumb_title))

        # Получение текста элемента
        text = element.text
        print(text)

        current_url = self.driver.current_url
        response = Http_methods.get(current_url)
        expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                     expected_value=200, url=current_url)

        self.wait.until(EC.element_to_be_clickable(self.link_to_home)).click()
        time.sleep(1)

    def click_all_links(self):
        for link_name in self.LINKS_DICT.keys():
            self.click_link(link_name)
