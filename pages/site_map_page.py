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
        # 'voting': ('xpath', '//a[@id="link_sitemap_stat_voting"]'),ddddd
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
        # 'config_callsschedule': ('xpath', '//a[@id="link_sitemap_config_callsschedule"]'),sss
        # 'config_voting': ('xpath', '//a[@id="link_sitemap_config_voting"]'),sss
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
        # 'edit_callsschedule': ('xpath', '//a[@id="link_sitemap_edit_callsschedule"]'),

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
    MAIN_TITLE = {
        'common': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Общая статистика',
        'commons': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по контактам',
        'agents': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по агентам',
        'calls': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по звонкам',
        'messages': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по сообщениям',
        'finalcategories': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по конечным категориям',
        'transfers': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по переводам',
        'extended': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Расширенные статистики',
        'xternal': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Внешние источники данных',
        'voting': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по анкетированию',
        # 'agentsrating': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по анкетированию',
        'agentsrating': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Рейтинг агентов',
        'objects': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по объектам',
        'chats': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по чатам',
        'attachments': os.getenv('ENVIRONMENT') + ' \\ Статистики \\ Статистика по вложениям',
        'config_main': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Общие настройки',
        'config_survey': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки опроса',
        'config_widgets': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки виджетов',
        'config_callprocessing': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки обзвона',
        'config_telephony': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки телефонии',
        'config_contactprocessing': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки обработки контакта',
        'config_stat': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки статистик',
        'config_importdata': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки импорта',
        'config_exportdata': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки экспорта',
        'config_operator': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки скрипта оператора',
        'config_customer': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Кабинет заказчика',
        'config_batchprocessing': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Пакетная обработка',
        'config_api': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ API',
        # 'config_callsschedule': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки расписаний звонков',sss
        # 'config_voting': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки анкетирования',sss
        'config_health': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Здоровье проекта',
        'config_callbackwidget': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Callback виджет',
        'config_objecttype': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Объекты',
        'config_chats': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки обработки чатов',
        'config_chat': os.getenv('ENVIRONMENT') + ' \\ Настройки \\ Настройки вложений',
        # Импорт/Экспорт
        'importdata_importdata': os.getenv('ENVIRONMENT') + ' \\ Импорт данных \\ Импорт',
        'importdata_yes_button': os.getenv('ENVIRONMENT') + ' \\ Карта проекта',
        'importdata_editimportdata': os.getenv('ENVIRONMENT') + ' \\ Импорт данных \\ Редактор импорта',
        'importdata_adminimportdata': os.getenv('ENVIRONMENT') + ' \\ Импорт данных \\ Управление импортом',
        'exportdata_exportdata': os.getenv('ENVIRONMENT') + ' \\ Экспорт данных \\ Экспорт',
        'exportdata_editexportdata': os.getenv('ENVIRONMENT') + ' \\ Экспорт данных \\ Редактop экспорта',
        # Редакторы
        'edit_survey': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор опроса',
        'edit_registries': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор реестров',
        'edit_finalcategories': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор конечных категорий',
        'edit_textcontent': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор текстового содержимого',
        'edit_navigationnodes': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактop навигации',
        'edit_filestorage': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Хранилище файлов',
        'edit_messages': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор сообщений',
        'edit_listtransfer': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор переводов',
        'edit_statuses': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор статусов',
        'edit_quotas': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор квот',
        'edit_catalogs': os.getenv('ENVIRONMENT'),
        'edit_callsschedule': os.getenv('ENVIRONMENT') + ' \\ Редакторы \\ Редактор расписаний звонков',

        #   Мониторинг
        'module_knowledgenodes': os.getenv('ENVIRONMENT') + ' \\ Модули \\ База знаний',
        'monitoring_telephony': os.getenv('ENVIRONMENT') + ' \\ Мониторинг \\ Телефония',
        'monitoring_activity': os.getenv('ENVIRONMENT') + ' \\ Мониторинг \\ Активность',
        'monitoring_services': os.getenv('ENVIRONMENT') + ' \\ Мониторинг \\ Сервисы',
        'monitoring_indicators': os.getenv('ENVIRONMENT') + ' \\ Мониторинг \\ Показатели проекта',
        'monitoring_health': os.getenv('ENVIRONMENT') + ' \\ Мониторинг \\ Здоровье проекта',
        #   Администрирование
        'admin_information': os.getenv('ENVIRONMENT') + ' \\ Администрирование \\ Информация о проекте',
        'admin_news': os.getenv('ENVIRONMENT') + ' \\ Администрирование \\ Новости',
        'admin_notifications': os.getenv('ENVIRONMENT') + ' \\ Администрирование \\ Уведомления',
        'admin_batchprocessing': os.getenv('ENVIRONMENT') + ' \\ Администрирование \\ Пакетная обработка',
        'admin_feedback': os.getenv('ENVIRONMENT') + ' \\ Администрирование \\ Обратная связь'
    }

    link_to_home = ('xpath', '//a[@href="/development/testing/sc240314_0000_testing_prohorov_2920/SiteMap.php"]')
    breadcrumb_title = ('xpath', '//span[@id="breadcrumb_title"]')

    def click_link(self, link_name: str):
        with allure.step(f'переход на {link_name}'):
            self.wait.until(EC.element_to_be_clickable(self.LINKS_DICT[link_name])).click()

            main_title = self.MAIN_TITLE.get(link_name, "")
            text = self.wait.until(EC.presence_of_element_located(self.breadcrumb_title)).text
            assert main_title == text, f"Название '{text}' не соответствует ожидаемому заголовку '{main_title}'"

            current_url = self.driver.current_url
            response = Http_methods.get(current_url)
            expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                         expected_value=200, url=current_url)

            self.wait.until(EC.element_to_be_clickable(self.link_to_home)).click()
            time.sleep(1)

    def click_all_links(self):
        for link_name in self.LINKS_DICT.keys():
            self.click_link(link_name)
