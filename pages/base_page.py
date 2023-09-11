"""Основные функции"""

from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://b2c.passport.rt.ru/'

    def open(self): # Открываем сайт
        self.driver.get(self.url)


    def element_is_visible(self, locator, timeout=10):  # Дожидаемся видимости элемента
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))