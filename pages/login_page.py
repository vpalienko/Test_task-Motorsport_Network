from _pytest.mark import ParameterSet

from data.project_urls import LOGIN_PAGE_URL
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = LOGIN_PAGE_URL
    locators = LoginPageLocators

    def enter_email(self, email: str | ParameterSet) -> None:
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password: str | ParameterSet) -> None:
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)

    def check_remember_me_checkbox(self) -> None:
        self.element_is_clickable(self.locators.REMEMBER_ME_CHECKBOX).click()

    def click_forgot_password_link(self) -> None:
        self.element_is_clickable(self.locators.FORGOT_PASSWORD_LINK).click()

    def click_sign_up_link(self) -> None:
        self.element_is_clickable(self.locators.SIGN_UP_LINK).click()

    def click_sign_in_button(self) -> None:
        self.element_is_clickable(self.locators.SIGN_IN_BUTTON).click()

    def should_be_login_form(self) -> None:
        assert self.is_element_present(self.locators.EMAIL_FIELD), "Email field is absent"
        assert self.is_element_present(self.locators.PASSWORD_FIELD), "Password field is absent"
        assert self.is_element_present(self.locators.FORGOT_PASSWORD_LINK), "Forgot password link is absent"
        assert self.is_element_present(self.locators.REMEMBER_ME_CHECKBOX), "Remember me checkbox is absent"
        assert self.is_element_present(self.locators.SIGN_IN_BUTTON), "Sign in button is absent"
        assert self.is_element_present(self.locators.SIGN_UP_LINK), "Sign up link is absent"

    def should_be_external_login_services(self) -> None:
        assert self.is_element_present(self.locators.FACEBOOK_LINK), "Facebook link is absent"
        assert self.is_element_present(self.locators.GOOGLE_LINK), "Google link is absent"
        assert self.is_element_present(self.locators.APPLE_LINK), "Apple link is absent"

    def should_be_error_alert(self) -> None:
        assert self.is_element_present(self.locators.ERROR_ALERT), "Error alert is absent"
        assert self.is_element_present(self.locators.ERROR_ALERT_TEXT), "Error alert text is absent"

    def should_be_email_field_error_message(self) -> None:
        assert self.is_element_present(self.locators.EMAIL_FIELD_ERROR_MESSAGE), "Email field error message is absent"

    def should_not_be_email_field_error_message(self) -> None:
        assert self.is_element_not_present(self.locators.EMAIL_FIELD_ERROR_MESSAGE), "Email field error message is present"

    def should_be_password_field_error_message(self) -> None:
        assert self.is_element_present(self.locators.PASSWORD_FIELD_ERROR_MESSAGE), "Password field error message is absent"

    def should_not_be_password_field_error_message(self) -> None:
        assert self.is_element_not_present(self.locators.PASSWORD_FIELD_ERROR_MESSAGE), "Password field error message is present"

    def email_field_should_be_prefilled_with_(self, user_email: str) -> None:
        email_field_locator = self.locators.EMAIL_FIELD
        assert self.is_element_present(email_field_locator), "Email field is absent"
        email_field_value = self.element_is_visible(email_field_locator).get_attribute("value")
        assert email_field_value == user_email, "Email field isn't pre-filled with user email"