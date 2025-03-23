from pytest import mark, param

from data.user_credentials import *


class TestLoginPage:

    class TestLoginPageContent:
        def test_login_page_can_be_opened(self, login_page, page):
            login_page.open()
            page.url_should_be_(login_page.url)
            login_page.should_be_login_form()
            login_page.should_be_external_login_services()

        def test_forgot_password_link_redirects_to_password_recovery_page(self, login_page, page):
            login_page.open()
            login_page.click_forgot_password_link()
            page.url_should_contain_("password/recovery")

        def test_sign_up_link_redirects_to_registration_page(self, login_page, page):
            login_page.open()
            login_page.click_sign_up_link()
            page.url_should_contain_("register")

    class TestAuthorization:
        def test_user_with_valid_credentials_can_be_logged_in(self, login_page, profile_page, page):
            login_page.open()
            login_page.enter_email(USER_EMAIL)
            login_page.enter_password(USER_PASSWORD)
            login_page.click_sign_in_button()
            page.url_should_be_(profile_page.url)
            profile_page.should_be_profile_page_content()
            profile_page.email_in_profile_should_correspond_to_(USER_EMAIL)

        def test_login_with_checked_remember_me_checkbox(self, login_page, profile_page, page):
            login_page.open()
            login_page.enter_email(USER_EMAIL)
            login_page.enter_password(USER_PASSWORD)
            login_page.check_remember_me_checkbox()
            login_page.click_sign_in_button()
            page.url_should_be_(profile_page.url)
            profile_page.click_log_out_link()
            page.url_should_be_(login_page.url)
            login_page.email_field_should_be_prefilled_with_(USER_EMAIL)

        def test_not_authorized_user_does_not_have_access_to_profile_page(self, profile_page, login_page, page):
            profile_page.open()
            page.url_should_be_(login_page.url)
            login_page.should_be_login_form()
            login_page.should_be_external_login_services()

    class TestInputFieldsValidation:
        @mark.parametrize("email,password", [param(USER_EMAIL, USER_WRONG_PASSWORD,
                                                   id="valid email and wrong password"),
                                             param(USER_WRONG_EMAIL, USER_PASSWORD,
                                                   id="wrong email and valid password"),
                                             param(DELETED_USER_EMAIL, DELETED_USER_PASSWORD,
                                                   id="email and password of deleted user")])
        def test_user_with_wrong_credentials_can_not_be_logged_in(self, login_page, page, email, password):
            login_page.open()
            login_page.enter_email(email)
            login_page.enter_password(password)
            login_page.click_sign_in_button()
            page.url_should_be_(login_page.url)
            login_page.should_be_error_alert()

        def test_user_with_empty_email_field_can_not_be_logged_in(self, login_page, page):
            login_page.open()
            login_page.enter_password(USER_PASSWORD)
            login_page.click_sign_in_button()
            page.url_should_be_(login_page.url)
            login_page.should_be_email_field_error_message()

        def test_user_with_empty_password_field_can_not_be_logged_in(self, login_page, page):
            login_page.open()
            login_page.enter_email(USER_EMAIL)
            login_page.click_sign_in_button()
            page.url_should_be_(login_page.url)
            login_page.should_be_password_field_error_message()

        def test_user_with_both_email_and_password_fields_empty_can_not_be_logged_in(self, login_page, page):
            login_page.open()
            login_page.click_sign_in_button()
            page.url_should_be_(login_page.url)
            login_page.should_be_email_field_error_message()
            login_page.should_be_password_field_error_message()

        @mark.parametrize("email", [param(USER_EMAIL_MIN_LENGTH_3, id="email min boundary value"),
                                    param(USER_EMAIL_MAX_LENGTH_100, id="email max boundary value")])
        def test_validation_email_field_for_valid_value(self, login_page, email):
            login_page.open()
            login_page.enter_email(email)
            login_page.click_sign_in_button()
            login_page.should_not_be_email_field_error_message()

        @mark.parametrize("password", [param(USER_PASSWORD_MIN_LENGTH_5, id="password min boundary value"),
                                       param(USER_PASSWORD_MAX_LENGTH_40, id="password max boundary value")])
        def test_validation_password_field_for_valid_value(self, login_page, password):
            login_page.open()
            login_page.enter_password(password)
            login_page.click_sign_in_button()
            login_page.should_not_be_password_field_error_message()

        @mark.parametrize("email", [param(USER_EMAIL_NOT_VALID, id="email value without '@' symbol"),
                                    param(USER_EMAIL_LESS_THAN_MIN_LENGTH_2, id="email less than min boundary value"),
                                    param(USER_EMAIL_MORE_THAN_MAX_LENGTH_101, id="email more than max boundary value")])
        def test_validation_email_field_for_not_valid_value(self, login_page, email):
            login_page.open()
            login_page.enter_email(email)
            login_page.click_sign_in_button()
            login_page.should_be_email_field_error_message()

        @mark.parametrize("password", [param(USER_PASSWORD_LESS_THAN_MIN_LENGTH_4, id="password less than min boundary value"),
                                       param(USER_PASSWORD_MORE_THAN_MAX_LENGTH_41, id="password more than max boundary value")])
        def test_validation_password_field_for_not_valid_value(self, login_page, password):
            login_page.open()
            login_page.enter_password(password)
            login_page.click_sign_in_button()
            login_page.should_be_password_field_error_message()