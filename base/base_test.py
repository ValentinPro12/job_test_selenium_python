import pytest
from config.data import Data
from outbound.pages.config.main_page import MainPage
from outbound.pages.config.survey_page import Survey
from pages.login_page import LoginPage
from pages.site_map_page import SiteMapPage


class BaseTest:
    """
    Класс для мельти-страница
    имеет метод setup является fixture
    """
    data: Data
    login_page: LoginPage
    site_map_page: SiteMapPage
    main_page: MainPage
    survey_page: Survey

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.data = Data
        request.cls.site_map_page = SiteMapPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.survey_page = Survey(driver)
