import allure
import pytest
from base.base_test import BaseTest


class TestPage(BaseTest):
    @allure.title('Проверка логина и перехода по всем пунктам меню ')
    @allure.severity('Critical')
    @pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_reg_input()
        self.site_map_page.is_opened()
        self.site_map_page.click_all_links()
