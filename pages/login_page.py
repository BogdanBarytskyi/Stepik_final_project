from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert 'login' in url, f'no such word "login" in {url}'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'no Login form here'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'no Register form here'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_NEW_USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_NEW_USER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_NEW_USER_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
