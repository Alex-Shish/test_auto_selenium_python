from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_REG_PASS_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_REG_PASS_2 = (By.CSS_SELECTOR, "#id_registration-password2")
