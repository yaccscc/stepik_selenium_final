from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email: str, password: str):
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        self.is_element_present(*LoginPageLocators.REGISTER_COMPLETE_MESSAGE)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "Url does not contain 'login' string"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"
        self.should_be_register_email_input()
        self.should_be_register_password_input()
        self.should_be_register_password_repeat_input()
        self.should_be_register_button()

    def should_be_register_email_input(self):
        self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_INPUT), \
            "Register email input is not presented"

    def should_be_register_password_input(self):
        self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_INPUT), \
            "Register password input is not presented"

    def should_be_register_password_repeat_input(self):
        self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_INPUT), \
            "Register password repeat input is not presented"

    def should_be_register_button(self):
        self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            "Register button is not presented"
