from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    FORGOT_PASSWORD_LINK = (By.ID, "restore_password")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "label[for='remember']")
    SIGN_IN_BUTTON = (By.ID, "submitbutton")
    SIGN_UP_LINK = (By.CSS_SELECTOR, ".have-account a")
    FACEBOOK_LINK = (By.ID, "facebook-submit")
    GOOGLE_LINK = (By.ID, "google-submit")
    APPLE_LINK = (By.ID, "apple-submit")
    ERROR_ALERT = (By.CLASS_NAME, "cmpTrayAlert")
    ERROR_ALERT_TEXT = (By.CSS_SELECTOR, ".cmpTrayAlert .text")
    EMAIL_FIELD_ERROR_MESSAGE = (By.ID, "email-error")
    PASSWORD_FIELD_ERROR_MESSAGE = (By.ID, "password-error")