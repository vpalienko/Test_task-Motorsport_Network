from data.project_urls import PROFILE_PAGE_URL
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    url = PROFILE_PAGE_URL
    locators = ProfilePageLocators

    def click_log_out_link(self) -> None:
        self.element_is_clickable(self.locators.LOGOUT_LINK).click()

    def should_be_profile_page_content(self) -> None:
        assert self.is_element_present(self.locators.PROFILE_MENU), "Profile menu is absent"
        assert self.is_element_present(self.locators.PROFILE_INFO), "Profile info is absent"
        assert self.is_element_present(self.locators.LOGOUT_LINK), "Logout link is absent"

    def email_in_profile_should_correspond_to_(self, user_email: str) -> None:
        profile_email_field_locator = self.locators.PROFILE_EMAIL_FIELD
        assert self.is_element_present(profile_email_field_locator), "Profile email field is absent"
        profile_email_field_value = self.element_is_visible(profile_email_field_locator).get_attribute("value")
        assert profile_email_field_value == user_email, "Email in profile doesn't correspond to user email"