from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_MENU = (By.ID, "layout_subnav")
    PROFILE_INFO = (By.ID, "user_info_block")
    PROFILE_EMAIL_FIELD = (By.CSS_SELECTOR, ".userDetailWrapper .fieldset:nth-child(2) input")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a.logout")