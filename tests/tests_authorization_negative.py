import time
from data_for_negative_test.data_for_test import DataForTests as data
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.page import Page

"""НЕГАТИВНЫЕ ТЕСТЫ НА СТРАНИЦЕ АВТОРИЗАЦИИ"""
class TestPageAuthorizationNegative:

    """Тестирование поля 'Телефон'"""
    class TestAuthorizationWithInvalidPhoneNumber:

        def test_authorization_with_wrong_phone_number(self, driver):  #  Проверяем, что появляется ошибка при вводе неверного номера
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.invalid_phone_number)  #  Вводим неверный номер
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  #  Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  #  Нажимаем Войти
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  #  Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  #  Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  #  Ошибка 'Неверно введен текст с картинки', в случае капчи
                assert 'Неверно введен текст с картинки' in error.text  #  Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_12_numbers(self, driver):  #  Проверяем, что поле "Телефон" не принимает больше 11 цифр
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            number = data.phone_number_more_11_numbers
            incorrect_phone_count_of_numbers = 0  #  Счетчик количества цифр неверного номера, просто чтобы был
            for i in number:
                Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(i)  # Вводим неверный номер по одной цифре, 12 цифр
                incorrect_phone_count_of_numbers += 1
            correct_phone_count_of_numbers = driver.find_element(By.XPATH, '//input[@type="hidden"][2]').get_attribute('value')  #  Максимальное количество введенных в поле цифр (поле не должно принимать больше 11)
            assert len(correct_phone_count_of_numbers) == 11  #  Проверяем, что поле не принимает количество цифр больше 11
            print(f'{incorrect_phone_count_of_numbers} > {len(correct_phone_count_of_numbers)}')  #  Печатаем просто для сравнения


        def test_authorization_with_10_numbers(self, driver):  #  Проверяем, что появляется ошибка при вводе номера менее 11 цифр
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.phone_number_less_11_numbers)  # Вводим неверный номер, 10 цифр
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Неверный формат телефона')]")))  #  Ошибка "Неверный формат телефона"
            assert 'Неверный формат телефона' in error.text  #  Проверяем, что появляется ошибка


        def test_authorization_with_kirillica_in_phone_number(self, driver):  #  Проверяем, что появиляется ошибка при вводе кириллицы и таб меняется на "Логин"
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.kirilica)  # Вводим кириллицу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            tab_login = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login')  #  Таб "Логин"
            assert 'Логин' in tab_login.text  #  Проверяем, что таб меняется на "Логин"
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  # Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки'
                assert 'Неверно введен текст с картинки' in error.text  # Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_latinica_in_phone_number(self, driver):  #  Проверяем, что появиляется ошибка при вводе латиницы и таб меняется на "Логин"
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.latinica)  # Вводим латиницу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            tab_login = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login')  #  Таб "Логин"
            assert 'Логин' in tab_login.text  #  Проверяем, что таб меняется на "Логин"
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  # Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки'
                assert 'Неверно введен текст с картинки' in error.text  # Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_specsimbols_in_phone_number(self, driver):  #  Проверяем, что появиляется ошибка при вводе спецсимволов и таб меняется на "Логин"
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.spec_simbols)  # Вводим спецсимволы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            tab_login = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login')  #  Таб "Логин"
            assert 'Логин' in tab_login.text  #  Проверяем, что таб меняется на "Логин"
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  # Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки'
                assert 'Неверно введен текст с картинки' in error.text  # Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_255_numbers(self, driver):  #  Проверяем, что появиляется ошибка при вводе 255 символов и таб меняется на "Логин"
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.simbols_255)  # Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            tab_login = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login')  #  Таб "Логин"
            assert 'Логин' in tab_login.text  #  Проверяем, что таб меняется на "Логин"
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  # Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки'
                assert 'Неверно введен текст с картинки' in error.text  # Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_1001_numbers(self, driver):  #  Проверяем, что появиляется ошибка при вводе 1001 символов и таб меняется на "Логин"
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.simbols_1001)  # Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            tab_login = driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login')  #  Таб "Логин"
            assert 'Логин' in tab_login.text  #  Проверяем, что таб меняется на "Логин"
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  # Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки'
                assert 'Неверно введен текст с картинки' in error.text  # Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_empty_field(self, driver):  #  Проверяем, что появиляется ошибка, если оставить поле "Телефон" пустым
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  #  Нажимаем на таб "Телефон"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).clear()  # Очищаем поле
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            error = driver.find_element(By.XPATH, "//span[contains(text(),'Введите номер телефона')]")  #  Ошибка "Введите номер телефона"
            assert 'Введите номер телефона' in error.text  #  Проверяем, что появляется ошибка

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Почта'"""
    class TestAuthorizationWithInvalidMail:

        def test_authorization_with_invalid_mail(self, driver):  #  Проверяем, что появляется ошибка при вводе неверного Email
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-mail'))).click()  # Нажимаем на таб "Почта"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.invalid_mail)  # Вводим неверную почту
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  #  Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  #  Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки', в случае капчи
                assert 'Неверно введен текст с картинки' in error.text  #  Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')

        def test_authorization_with_empty_field_of_email(self, driver):  #  Проверяем, что появляется ошибка если оставить пустое поле Email
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-mail'))).click()  # Нажимаем на таб "Почта"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).clear()  # Очищаем поле Email
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите адрес, указанный при регистрации')]")))  #  Ошибка 'Введите адрес, указанный при регистрации'
            assert "Введите адрес" in error.text  #  Проверяем, что появляется ошибка


            """Остальные тесты такие же как и с номером телефона, поле ввода одно"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Логин'"""
    class TestAuthorizationWithInvalidLogin:

        def test_authorization_with_invalid_login(self, driver):  #  Проверяем, что появляется ошибка при вводе неверного логина
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-login'))).click()  # Нажимаем на таб "Логин"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.invalid_login)  # Вводим неверный логин
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  #  Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  #  Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки', в случае капчи
                assert 'Неверно введен текст с картинки' in error.text  #  Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_empty_field_of_login(self, driver):  #  Проверяем, что появляется ошибка если оставить пустое поле Логин
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-login'))).click()  # Нажимаем на таб "Логин"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).clear()  # Очищаем поле Логин
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите логин, указанный при регистрации')]")))  #  Ошибка 'Введите логин, указанный при регистрации'
            assert "Введите логин" in error.text  #  Проверяем, что появляется ошибка

        """Остальные тесты такие же как и с номером телефона и почты, поле ввода одно"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Лицевой счет'"""
    class TestAuthorizationWithInvalidPersonalAccount:

        """Поле Лицевой счет принимает только цифры, состоит из 12 цифр"""

        def test_authorization_with_invalid_personal_account(self, driver):  #  Проверяем, что появляется ошибка при вводе неверного лицевого счета
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  # Нажимаем на таб "Лицевой счет"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.invalid_personal_account)  # Вводим неверный лицевой счет
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  # Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                 '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки', в случае капчи
                assert 'Неверно введен текст с картинки' in error.text  # Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')


        def test_authorization_with_kirillica_in_personal_account(self, driver):  #  Проверяем, что после ввода кириллицы поле ввода Лицевой счет остается пустым и появляется ошибка
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  # Нажимаем на таб "Лицевой счет"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.kirilica)  # Вводим кириллицу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            empty_field_of_personal_account = driver.find_element(By.XPATH, '//input[@type="hidden"][2]').get_attribute('value')  #  Пустое поле Лицевой счет после ввода кириллицы
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите номер вашего лицевого счета')]")))  #  Ошибка "Введите номер вашего лицевого счета"
            assert empty_field_of_personal_account == ''  #  Проверяем, что поле ввода осталось пустым
            assert 'Введите номер вашего лицевого счета' in error.text  #  Проверяем, что появилась ошибка


        def test_authorization_with_latinica_in_personal_account(self, driver):  #  Проверяем, что после ввода латиницу поле ввода Лицевой счет остается пустым и появляется ошибка
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  # Нажимаем на таб "Лицевой счет"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.latinica)  # Вводим латиницу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            empty_field_of_personal_account = driver.find_element(By.XPATH, '//input[@type="hidden"][2]').get_attribute('value')  #  Пустое поле Лицевой счет после ввода латиницы
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите номер вашего лицевого счета')]")))  #  Ошибка "Введите номер вашего лицевого счета"
            assert empty_field_of_personal_account == ''  #  Проверяем, что поле ввода осталось пустым
            assert 'Введите номер вашего лицевого счета' in error.text  #  Проверяем, что появилась ошибка


        def test_authorization_with_specsimbols_in_personal_account(self, driver):  #  Проверяем, что после ввода спецсимволов поле ввода Лицевой счет остается пустым и появляется ошибка
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  # Нажимаем на таб "Лицевой счет"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.spec_simbols)  # Вводим спецсимволы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            empty_field_of_personal_account = driver.find_element(By.XPATH, '//input[@type="hidden"][2]').get_attribute('value')  #  Пустое поле Лицевой счет после ввода спецсимволов
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите номер вашего лицевого счета')]")))  #  Ошибка "Введите номер вашего лицевого счета"
            assert empty_field_of_personal_account == ''  #  Проверяем, что поле ввода осталось пустым
            assert 'Введите номер вашего лицевого счета' in error.text  #  Проверяем, что появилась ошибка


        def test_authorization_of_personal_account_with_13_numbers(self, driver):  #  Проверяем, что поле "Лицевой счет" не принимает больше 12 цифр
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  # Нажимаем на таб "Лицевой счет"
            number = data.personal_account_more_12_numbers
            incorrect_personal_account = 0  #  Счетчик количества цифр лицевого счета, просто чтобы был
            for i in number:
                driver.find_element(By.CSS_SELECTOR, "#username").send_keys(i)  # Вводим лицевой счет по одной цифре, 13 цифр
                incorrect_personal_account += 1
            correct_personal_account = driver.find_element(By.XPATH, '//input[@type="hidden"][2]').get_attribute('value')  #  Максимальное количество введенных в поле цифр (поле не должно принимать больше 12)
            assert len(correct_personal_account) == 12  #  Проверяем, что поле не принимает количество цифр больше 12
            print(f'{incorrect_personal_account} > {len(correct_personal_account)}')  #  Печатаем просто для сравнения


        def test_authorization_of_personal_account_with_11_numbers(self, driver):  #  Проверяем, что появляется ошибка при вводе лицевого счета менее 12 цифр
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  # Нажимаем на таб "Лицевой счет"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).send_keys(data.personal_account_less_12_numbers)  # Вводим неверный лицевой счет, 11 цифр
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Проверьте, пожалуйста, номер лицевого счета')]")))  #  Ошибка "Проверьте, пожалуйста, номер лицевого счета"
            assert 'Проверьте, пожалуйста, номер лицевого счета' in error.text  #  Проверяем, что появляется ошибка


        def test_authorization_with_empty_field_of_personal_account(self, driver):  #  Проверяем, что появляется ошибка если оставить пустое поле Лицевой счет
            page = Page(driver)
            page.open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  # Нажимаем на таб "Лицевой счет"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#username"))).clear()  # Очищаем поле Лицевой счет
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).send_keys(data.valid_password)  # Вводим верный пароль
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#kc-login'))).click()  # Нажимаем Войти
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите номер вашего лицевого счета')]")))  #  Ошибка 'Введите номер вашего лицевого счета'
            assert "Введите номер вашего лицевого счета" in error.text  #  Проверяем, что появляется ошибка


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование авторизации с неверным паролем"""
    class TestAuthorizationWithInvalidPassword:

        def test_authorization_with_valid_email_and_invalid_password(self, driver):  #  Проверяем, что появляется ошибка при вводе неверного пароля
            page = Page(driver)
            page.open()
            page.authorization_form_fill_fields_and_submit_with_valid_email_and_invalid_password()
            try:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#form-error-message')))  # Ошибка 'Неверный логин или пароль'
                assert 'Неверный логин или пароль' in error.text  # Если номер неверный появляется эта ошибка
                print('Неверный логин или пароль')
            except:
                error = Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                 '#form-error-message')))  # Ошибка 'Неверно введен текст с картинки', в случае капчи
                assert 'Неверно введен текст с картинки' in error.text  # Ошибка появляется, когда появляется капча
                print('Неверно введен текст с картинки')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------