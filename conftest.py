from typing import Generator

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@fixture
def driver() -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@fixture
def page(driver: WebDriver) -> BasePage:
    return BasePage(driver)


@fixture
def login_page(driver: WebDriver) -> LoginPage:
    return LoginPage(driver)


@fixture
def profile_page(driver: WebDriver) -> ProfilePage:
    return ProfilePage(driver)