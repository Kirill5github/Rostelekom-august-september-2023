from data_for_negative_test.data_for_test import DataForTests as data
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.page import Page

"""НЕГАТИВНЫЕ ТЕСТЫ НА СТРАНИЦЕ РЕГИСТРАЦИИ"""
class TestPageRegistrationNegative:

    """Тестирование поля 'Имя'"""
    class TestRegistrationFieldName:

        """Поле 'Имя' принимает только кириллицу, от 2 до 30 символов"""

        def test_registration_field_name_with_2_letters_kirillica(self, driver):  #  Проверка поля "Имя", ввод 2 буквы кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_kirillica_2)  #  Вводим 2 буквы кириллицей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="card-container__content"]')))  #  Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  #  Проверяем, что ошибка не появляется, поле принимает 2 буквы как имя


        def test_registration_field_name_with_2_letters_latinica(self, driver):  #  Проверка поля "Имя", ввод 2 буквы латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_latinica_2)  #  Вводим 2 буквы латиницей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_1_letter_kirillica(self, driver):  #  Проверка поля "Имя", ввод 1 буквы кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_kirillica_1)  #  Вводим 1 букву кириллицей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_1_letter_latinica(self, driver):  #  Проверка поля "Имя", ввод 1 буквы латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_latinica_1)  #  Вводим 1 букву латиницей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_29_letters_kirillica(self, driver):  #  Проверка поля "Имя", ввод 29 букв кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_kirillica_29)  #  Вводим 29 букв кириллицей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="card-container__content"]')))  #  Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  #  Проверяем, что ошибка не появляется, поле принимает 29 букв как имя


        def test_registration_field_name_with_29_letters_latinica(self, driver):  #  Проверка поля "Имя", ввод 29 букв латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_latinica_29)  #  Вводим 29 букв латиницей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_30_letters_kirillica(self, driver):  #  Проверка поля "Имя", ввод 30 букв кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_kirillica_30)  #  Вводим 30 букв кириллицей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="card-container__content"]')))  #  Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  #  Проверяем, что ошибка не появляется, поле принимает 30 букв как имя


        def test_registration_field_name_with_30_letters_latinica(self, driver):  #  Проверка поля "Имя", ввод 30 букв латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_latinica_30)  #  Вводим 30 букв латиницей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_31_letters_kirillica(self, driver):  #  Проверка поля "Имя", ввод 31 буквы кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_kirillica_31)  #  Вводим 31 букву кириллицей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_31_letters_latinica(self, driver):  #  Проверка поля "Имя", ввод 31 буквы латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.letter_latinica_31)  #  Вводим 31 букву латиницей
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_specsimbols(self, driver):  #  Проверка поля "Имя", ввод спецсимволов
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.spec_simbols)  #  Вводим спецсимволы
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_255_simbols(self, driver):  #  Проверка поля "Имя", ввод 255 символов
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.simbols_255_kirillica)  #  Вводим символы
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_1001_simbols(self, driver):  #  Проверка поля "Имя", ввод 1001 символ
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.simbols_1001_kirillica)  #  Вводим символы
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_empty_field(self, driver):  #  Проверка поля "Имя", пустое поле
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).clear()  #  Очищаем поле
            driver.find_element(By.NAME, 'register').click()  #  Нажимаем на кнопку "Зарегестрироваться"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_name_with_tire_in_name_between(self, driver):  #  Проверка поля "Имя", с тире в середине имени
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.name_with_tire_between)  #  Вводим имя с тире посередине
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="card-container__content"]')))  # Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  # Проверяем, что ошибка не появляется, поле принимает имя с тире посередине


        def test_registration_field_name_with_tire_in_name_first(self, driver):  #  Проверка поля "Имя", поле не принимает имя с тире в начале
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).send_keys(data.name_with_tire)  #  Вводим имя начиная с тире
            driver.find_element(By.NAME, 'lastName').click()  #  Нажимаем на поле "Фамилия"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Фамилия'"""
    class TestRegistrationFieldLastName:

        """Поле 'Фамилия' принимает только кириллицу, от 2 до 30 символов"""

        def test_registration_field_lastname_with_2_letters_kirillica(self, driver):  #  Проверка поля "Фамилия", ввод 2 буквы кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_kirillica_2)  #  Вводим 2 буквы кириллицей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="card-container__content"]')))  #  Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  #  Проверяем, что ошибка не появляется, поле принимает 2 буквы как имя


        def test_registration_field_lastname_with_2_letters_latinica(self, driver):  #  Проверка поля "Фамилия", ввод 2 буквы латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_latinica_2)  #  Вводим 2 буквы латиницей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_1_letter_kirillica(self, driver):  #  Проверка поля "Фамилия", ввод 1 буквы кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_kirillica_1)  #  Вводим 1 букву кириллицей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_1_letter_latinica(self, driver):  #  Проверка поля "Фамилия", ввод 1 буквы латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_latinica_1)  #  Вводим 1 букву латиницей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_29_letters_kirillica(self, driver):  #  Проверка поля "Фамилия", ввод 29 букв кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_kirillica_29)  #  Вводим 29 букв кириллицей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="card-container__content"]')))  #  Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  #  Проверяем, что ошибка не появляется, поле принимает 29 букв как имя


        def test_registration_field_lastname_with_29_letters_latinica(self, driver):  #  Проверка поля "Фамилия", ввод 29 букв латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_latinica_29)  #  Вводим 29 букв латиницей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_30_letters_kirillica(self, driver):  #  Проверка поля "Фамилия", ввод 30 букв кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_kirillica_30)  #  Вводим 30 букв кириллицей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="card-container__content"]')))  #  Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  #  Проверяем, что ошибка не появляется, поле принимает 30 букв как имя


        def test_registration_field_lastname_with_30_letters_latinica(self, driver):  #  Проверка поля "Фамилия", ввод 30 букв латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_latinica_30)  #  Вводим 30 букв латиницей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_31_letters_kirillica(self, driver):  #  Проверка поля "Фамилия", ввод 31 буквы кириллицей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_kirillica_31)  #  Вводим 31 букву кириллицей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_31_letters_latinica(self, driver):  #  Проверка поля "Фамилия", ввод 31 буквы латиницей
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.letter_latinica_31)  #  Вводим 31 букву латиницей
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_specsimbols(self, driver):  #  Проверка поля "Фамилия", ввод спецсимволов
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.spec_simbols)  #  Вводим спецсимволы
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_255_simbols(self, driver):  #  Проверка поля "Фамилия", ввод 255 символов
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.simbols_255_kirillica)  #  Вводим символы
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_1001_simbols(self, driver):  #  Проверка поля "Фамилия", ввод 1001 символ
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.simbols_1001_kirillica)  #  Вводим символы
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_empty_field(self, driver):  #  Проверка поля "Фамилия", пустое поле
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).clear()  #  Очищаем поле
            driver.find_element(By.NAME, 'register').click()  #  Нажимаем на кнопку "Зарегестрироваться"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_lastname_with_tire_in_lastname_between(self, driver):  #  Проверка поля "Фамилия", с тире в середине фамилии
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.lastname_with_tire_between)  #  Вводим фамилию с тире посередине
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            fields_container = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="card-container__content"]')))  # Блок со всеми полями, так же ошибка появляется в этом блоке
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' not in fields_container.text  # Проверяем, что ошибка не появляется, поле принимает имя с тире посередине


        def test_registration_field_lastname_with_tire_in_lastname_first(self, driver):  #  Проверка поля "Фамилия", поле не принимает фамилию с тире в начале
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'lastName'))).send_keys(data.lastname_with_tire)  #  Вводим фамилию начиная с тире
            driver.find_element(By.NAME, 'firstName').click()  #  Нажимаем на поле "Имя"
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))  #  Ошибка "Необходимо заполнить поле кириллицей. От 2 до 30 с"
            assert 'Необходимо заполнить поле кириллицей. От 2 до 30 с' in error.text  #  Проверяем, что появляется ошибка

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Регион'"""
    class TestRegistrationFieldRegion:

        """По умолчанию регион выбран Москва"""

        def test_registration_field_region_with_kirillica(self, driver):  # Проверка поля Регион, кириллица
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список, и слово Москва выделилось
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(data.kirilica)  #  Вводим кириллицу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).click()  #  Нажимаем на поле Имя
            driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
            region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'Москва')]")))  #  Регион, который устанавливается по умолчанию, в случае ввода неверного региона
            assert 'Москва' in region.text  #  Ошибки нет, но введенные символы меняются на регион по умолчанию - Москва


        def test_registration_field_region_with_latinica(self, driver):  # Проверка поля Регион, латиница
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список, и слово Москва выделилось
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(data.latinica)  #  Вводим латиницу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).click()  #  Нажимаем на поле Имя
            driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
            region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'Москва')]")))  #  Регион, который устанавливается по умолчанию, в случае ввода неверного региона
            assert 'Москва' in region.text  #  Ошибки нет, но введенные символы меняются на регион по умолчанию - Москва


        def test_registration_field_region_with_specsimbols(self, driver):  # Проверка поля Регион, спецсимволы
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список, и слово Москва выделилось
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(data.spec_simbols)  #  Вводим спецсимволы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).click()  #  Нажимаем на поле Имя
            driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
            region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'Москва')]")))  #  Регион, который устанавливается по умолчанию, в случае ввода неверного региона
            assert 'Москва' in region.text  #  Ошибки нет, но введенные символы меняются на регион по умолчанию - Москва


        def test_registration_field_region_with_255_simbols(self, driver):  # Проверка поля Регион, 255 символов
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список, и слово Москва выделилось
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(data.simbols_255)  #  Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).click()  #  Нажимаем на поле Имя
            driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
            region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'Москва')]")))  #  Регион, который устанавливается по умолчанию, в случае ввода неверного региона
            assert 'Москва' in region.text  #  Ошибки нет, но введенные символы меняются на регион по умолчанию - Москва


        def test_registration_field_region_with_1001_simbols(self, driver):  # Проверка поля Регион, 1001 символ
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список, и слово Москва выделилось
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(data.simbols_1001)  #  Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).click()  #  Нажимаем на поле Имя
            driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
            region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'Москва')]")))  #  Регион, который устанавливается по умолчанию, в случае ввода неверного региона
            assert 'Москва' in region.text  #  Ошибки нет, но введенные символы меняются на регион по умолчанию - Москва


        def test_registration_field_region_with_numbers(self, driver):  # Проверка поля Регион, цифры
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список, и слово Москва выделилось
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(data.numbers)  #  Вводим цифры
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).click()  #  Нажимаем на поле Имя
            driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
            region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'Москва')]")))  #  Регион, который устанавливается по умолчанию, в случае ввода неверного региона
            assert 'Москва' in region.text  #  Ошибки нет, но введенные символы меняются на регион по умолчанию - Москва


        def test_registration_field_region_with_empty_field(self, driver):  # Проверка поля Регион, пустое поле
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список, и слово Москва выделилось
            Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(' ')  #  Очищаем поле
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).click()  #  Нажимаем на поле Имя
            driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
            region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'Москва')]")))  #  Регион, который устанавливается по умолчанию, в случае ввода неверного региона
            assert 'Москва' in region.text  #  Ошибки нет, но введенные символы меняются на регион по умолчанию - Москва

            """При вводе чего угодно, либо оставлении поля пустым, поле автоматически заполняется регионом по умолчанию Москва"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Email и мобильный телефон'"""

    class TestRegistrationFieldEmailAndPhone:

        def test_registration_field_email_and_phone_with_kirillica(self, driver):  #  Проверка поля "Email и мобильный телефон", кириллица
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#address'))).send_keys(data.kirilica)  #  Вводим кириллицу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).click()  # Нажимаем на поле пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  #  Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_email_and_phone_with_latinica(self, driver):  #  Проверка поля "Email и мобильный телефон", латиница
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#address'))).send_keys(data.latinica)  #  Вводим латиницу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).click()  # Нажимаем на поле пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  #  Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_email_and_phone_with_specsimbols(self, driver):  #  Проверка поля "Email и мобильный телефон", спецсимволы
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#address'))).send_keys(data.spec_simbols)  #  Вводим спецсимволы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).click()  # Нажимаем на поле пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  #  Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_email_and_phone_with_255_simbols(self, driver):  #  Проверка поля "Email и мобильный телефон", 255 символов
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#address'))).send_keys(data.simbols_255)  #  Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).click()  # Нажимаем на поле пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  #  Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_email_and_phone_with_1001_simbols(self, driver):  #  Проверка поля "Email и мобильный телефон", 1001 символ
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#address'))).send_keys(data.simbols_1001)  #  Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password'))).click()  # Нажимаем на поле пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  #  Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  #  Проверяем, что появляется ошибка


        def test_registration_field_email_and_phone_with_empty_field(self, driver):  #  Проверка поля "Email и мобильный телефон", пустое поле
            page = Page(driver)
            page.open()
            page.registration_form_open()
            page.registration_form_fill_fields_and_submit_with_valid_data_without_field_email()
            driver.find_element(By.NAME, 'register').click()
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  # Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  # Проверяем, что появляется ошибка


        def test_registration_field_email_and_phone_with_10_numbers(self, driver):  #  Проверка поля "Email и мобильный телефон", 10 цифр
            page = Page(driver)
            page.open()
            page.registration_form_open()
            page.registration_form_fill_fields_and_submit_with_valid_data_without_field_email()  #  Заполняем все поля кроме Email
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='address']"))).send_keys(data.phone_number_less_11_numbers)  #  Вводим цифры
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()  #  Нажимаем Зарегестрироваться
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  # Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  # Проверяем, что появляется ошибка


        def test_registration_field_email_and_phone_with_12_numbers(self, driver):  #  Проверка поля "Email и мобильный телефон", 12 цифр
            page = Page(driver)
            page.open()
            page.registration_form_open()
            page.registration_form_fill_fields_and_submit_with_valid_data_without_field_email()  #  Заполняем все поля кроме Email
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='address']"))).send_keys(data.phone_number_more_11_numbers)  #  Вводим цифры
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'register'))).click()  #  Нажимаем Зарегестрироваться
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))  # Ошибка 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
            assert 'телефон' and 'email' in error.text  # Проверяем, что появляется ошибка

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Пароль'"""

    class TestRegistrationFieldPassword:

        """Пароль должен быть не менее 8 и не более 20 символов, только латиница, содержать заглавные и строчные буквы, также хотя бы одну цифру или спецсимвол"""

        def test_registration_field_password_with_kirillica(self, driver):  #  Проверка поля "Пароль", кириллица
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(data.password_kirillica)  #  Вводим кириллицу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()  #  Нажимаем на поле Подтверждение пароля
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Пароль должен содержать только латинские буквы')]")))  #  Ошибка "Пароль должен содержать только латинские буквы"
            assert 'только латинские' in error.text  #  Проверяем, что появилась ошибка


        def test_registration_field_password_with_21_simbols(self, driver):  #  Проверка поля "Пароль", 21 символ, соблюдая остальные требования пароля
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(data.password_21)  #  Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()  #  Нажимаем на поле Подтверждение пароля
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Длина пароля должна быть не более 20 символов')]")))  #  Ошибка "Длина пароля должна быть не более 20 символов"
            assert 'не более 20' in error.text  #  Проверяем, что появилась ошибка


        def test_registration_field_password_with_specsimbols(self, driver):  #  Проверка поля "Пароль", спецсимволы
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(data.password_specsimbols)  #  Вводим спецсимволы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()  #  Нажимаем на поле Подтверждение пароля
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Пароль должен содержать хотя бы одну заглавную бук')]")))  #  Ошибка "Пароль должен содержать хотя бы одну заглавную букву"
            assert 'заглавную букву' in error.text  #  Проверяем, что появилась ошибка


        def test_registration_field_password_with_numbers(self, driver):  #  Проверка поля "Пароль", цифры
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(data.password_numbers)  #  Вводим цифры
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()  #  Нажимаем на поле Подтверждение пароля
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Пароль должен содержать хотя бы одну заглавную бук')]")))  #  Ошибка "Пароль должен содержать хотя бы одну заглавную букву"
            assert 'заглавную букву' in error.text  #  Проверяем, что появилась ошибка


        def test_registration_field_password_less_8_simbols(self, driver):  #  Проверка поля "Пароль", менее 8 символов, соблюдая остальные требования
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(data.password_less_8_numbers)  #  Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()  #  Нажимаем на поле Подтверждение пароля
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Длина пароля должна быть не менее 8 символов')]")))  #  Ошибка "Длина пароля должна быть не менее 8 символов"
            assert 'не менее 8' in error.text  #  Проверяем, что появилась ошибка


        def test_registration_field_password_caps_simbols(self, driver):  #  Проверка поля "Пароль", все заглавные буквы, соблюдая остальные требования
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(data.password_caps)  #  Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).click()  #  Нажимаем на поле Подтверждение пароля
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Пароль должен содержать хотя бы одну строчную букв')]")))  #  Ошибка "Пароль должен содержать хотя бы одну строчную букву"
            assert 'строчную букву' in error.text  #  Проверяем, что появилась ошибка


        def test_registration_field_password_with_empty_field(self, driver):  #  Проверка поля "Пароль", пустое поле
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(data.name)  #  Заполняем поле Имя
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "lastName"))).send_keys(data.last_name)  #  Заполняем поле Фамилия
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='address']"))).send_keys(data.valid_email)  #  Заполняем поле Почта
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(data.valid_password)  #  Вводим валидный пароль в поле "Подтверждение пароля"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "register"))).click()  #  Нажимаем Зарегестрироваться
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Длина пароля должна быть не менее 8 символов')]")))  #  Ошибка "Длина пароля должна быть не менее 8 символов"
            assert 'не менее 8' in error.text  #  Проверяем, что появилась ошибка

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование поля 'Подтверждение пароля'"""

    class TestRegistrationFieldConfirmPassword:
        """Пароль должен быть не менее 8 и не более 20 символов, только латиница, содержать заглавные и строчные буквы, также хотя бы одну цифру или спецсимвол"""

        def test_registration_field_confirm_password_with_kirillica(self, driver):  # Проверка поля "Подтверждение пароля", кириллица
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(data.password_kirillica)  # Вводим кириллицу
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).click()  # Нажимаем на поле Пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Пароль должен содержать только латинские буквы')]")))  # Ошибка "Пароль должен содержать только латинские буквы"
            assert 'только латинские' in error.text  # Проверяем, что появилась ошибка


        def test_registration_field_confirm_password_with_21_simbols(self, driver):  # Проверка поля "Подтверждение пароля", 21 символ, соблюдая остальные требования пароля
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(data.password_21)  # Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).click()  # Нажимаем на поле Пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Длина пароля должна быть не более 20 символов')]")))  # Ошибка "Длина пароля должна быть не более 20 символов"
            assert 'не более 20' in error.text  # Проверяем, что появилась ошибка


        def test_registration_field_confirm_password_with_specsimbols(self, driver):  # Проверка поля "Подтверждение пароля", спецсимволы
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(data.password_specsimbols)  # Вводим спецсимволы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).click()  # Нажимаем на поле Пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Пароль должен содержать хотя бы одну заглавную бук')]")))  # Ошибка "Пароль должен содержать хотя бы одну заглавную букву"
            assert 'заглавную букву' in error.text  # Проверяем, что появилась ошибка


        def test_registration_field_confirm_password_with_numbers(self, driver):  # Проверка поля "Подтверждение пароля", цифры
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(data.password_numbers)  # Вводим цифры
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).click()  # Нажимаем на поле Пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Пароль должен содержать хотя бы одну заглавную бук')]")))  # Ошибка "Пароль должен содержать хотя бы одну заглавную букву"
            assert 'заглавную букву' in error.text  # Проверяем, что появилась ошибка


        def test_registration_field_confirm_password_less_8_simbols(self, driver):  # Проверка поля "Подтверждение пароля", менее 8 символов, соблюдая остальные требования
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(data.password_less_8_numbers)  # Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).click()  # Нажимаем на поле Пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Длина пароля должна быть не менее 8 символов')]")))  # Ошибка "Длина пароля должна быть не менее 8 символов"
            assert 'не менее 8' in error.text  # Проверяем, что появилась ошибка


        def test_registration_field_confirm_password_caps_simbols(self, driver):  # Проверка поля "Подтверждение пароля", все заглавные буквы, соблюдая остальные требования
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-confirm']"))).send_keys(data.password_caps)  # Вводим символы
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).click()  # Нажимаем на поле Пароль
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Пароль должен содержать хотя бы одну строчную букв')]")))  # Ошибка "Пароль должен содержать хотя бы одну строчную букву"
            assert 'строчную букву' in error.text  # Проверяем, что появилась ошибка


        def test_registration_field_confirm_password_with_empty_field(self, driver):  # Проверка поля "Подтверждение пароля", пустое поле
            page = Page(driver)
            page.open()
            page.registration_form_open()
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(data.name)  # Заполняем поле Имя
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "lastName"))).send_keys(data.last_name)  # Заполняем поле Фамилия
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='address']"))).send_keys(data.valid_email)  # Заполняем поле Почта
            Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(data.valid_password)  # Вводим валидный пароль в поле "Пароль"
            Wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "register"))).click()  # Нажимаем Зарегестрироваться
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Длина пароля должна быть не менее 8 символов')]")))  # Ошибка "Длина пароля должна быть не менее 8 символов"
            assert 'не менее 8' in error.text  # Проверяем, что появилась ошибка

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    """Тестирование регистрации с существующей учетной записью"""

    class TestAuthorizationWitnExistAccount:

        def test_registration_with_exist_account(self, driver):  #  Проверка регистрации с существующей учетной записью
            page = Page(driver)
            page.open()
            page.registration_form_open()
            page.registration_with_exist_account()  #  Заполняем поля с зарегестрированным Email
            error = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Учётная запись уже существует')]")))  #  Ошибка "Учётная запись уже существует"
            assert 'Учётная запись уже существует' in error.text