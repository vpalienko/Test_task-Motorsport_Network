from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    url = None

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.url)

    def element_is_visible(self, locator: tuple[str, str], timeout: int | float = 5) -> WebElement:
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_not_visible(self, locator: tuple[str, str], timeout: int | float = 5) -> WebElement:
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator: tuple[str, str], timeout: int | float = 5) -> WebElement:
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def is_element_present(self, locator: tuple[str, str], timeout: int | float = 5) -> bool:
        try:
            self.element_is_visible(locator, timeout)
        except TimeoutException:
            return False
        return True

    def is_element_not_present(self, locator: tuple[str, str], timeout: int | float = 5) -> bool:
        try:
            self.element_is_not_visible(locator, timeout)
        except TimeoutException:
            return False
        return True

    def url_should_contain_(self, text: str, timeout: int | float = 1) -> None:
        is_contain = True
        try:
            wait(self.driver, timeout).until(EC.url_contains(text))
        except TimeoutException:
            is_contain = False
        assert is_contain, f"Current page URL '{self.driver.current_url}' doesn't contain '{text}'"

    def url_should_be_(self, url: str, timeout: int | float = 1) -> None:
        is_match = True
        try:
            wait(self.driver, timeout).until(EC.url_to_be(url))
        except TimeoutException:
            is_match = False
        assert is_match, f"Current page URL '{self.driver.current_url}' doesn't match '{url}'"