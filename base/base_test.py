import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.site_map_page import SiteMapPage


class BaseTest:
    data: Data
    login_page: LoginPage
    site_map_page: SiteMapPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.data = Data
        request.cls.site_map_page = SiteMapPage(driver)
