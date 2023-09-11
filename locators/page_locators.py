"""��������"""

from selenium.webdriver.common.by import By

class PageLocators:
    """�������� ��� �����������, ����� � ������"""
    EMAIL_TAB = (By.CSS_SELECTOR, '#t-btn-tab-mail')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#username')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    BUTTON_ENTER = (By.CSS_SELECTOR, '#kc-login')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, '#logout-btn')


    """�������� ��� ����������� �� �����"""
    FIRST_NAME = (By.XPATH, '//input[@name="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@name="lastName"]')
    REGION = (By.XPATH, '//input[@xpath="1"]')
    EMAIL = (By.CSS_SELECTOR, '#address')
    PASSWORD_FIRST = (By.CSS_SELECTOR, '#password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#password-confirm')
    BUTTON_REGISTER = (By.XPATH, '//button[@name="register"]')


    """�������� ������ �� ����� ����������� � �������������� ������"""
    REGISTRATION_FORM_LINK = (By.CSS_SELECTOR, '#kc-register')
    FORGOT_PASSWORD_FORM_LINK = (By.CSS_SELECTOR, '#forgot_password')

    """������� ������ �� ���������������� ����������"""
    TERMS_OF_USE_LINK = (By.XPATH, '//form/div/a[@href="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"]')