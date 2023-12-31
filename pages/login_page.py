from .base_page import BasePage
from .locators import LoginPageLocators

url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def should_be_login_url():
    login_link = BasePage.open().find_element(*LoginPageLocators.LOGIN_LINK)
    login_link.click()


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True
