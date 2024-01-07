from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class ProductPage(BasePage):
    def should_be_control_url(self):
        assert self.is_element_present(*BasketPageLocators.ADD_BASKET), "Login link is not presented"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.ADD_BASKET)
        basket_link.click()
        return ProductPage(browser=self.browser, url=self.browser.current_url)
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")