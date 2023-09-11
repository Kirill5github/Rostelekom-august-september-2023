import random
import mouse

from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.page import Page

"""ПОЗИТИВНЫЕ ТЕСТЫ"""
class TestPagePositive:

    """Тестирование авторизации с валидными данными"""
    def test_authorization_with_valid_data(self, driver): # Проверяем, что авторизация проходит успешно, вход на сайт и выход на форму авторизации
        page = Page(driver)
        page.open()
        page.authorization_form_fill_fields_and_submit_with_valid_data()
        user_data_in_account = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="base-card home__info-card"]')))    # Страница с учетными данными
        assert 'Учетные данные' in user_data_in_account.text
        page.logout_button_push()
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  #  Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование табов 'Телефон', 'Почта', 'Логин', 'Лицевой счет'"""
    def test_tabs_of_authorization_and_slogan(self, driver):  #  Проверяем, что табы выбора авторизации "Телефон", "Почта", "Логин", "Лицевой счет", переключаются и их возможно заполнить, также есть слоган Ростелекома
        page = Page(driver)
        page.open()
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()  #  Таб "Лицевой счет"
        Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys('111111111111')  #  Зполняем поле "Лицевой счет", данные вымышлены
        field_personal_account = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Лицевой счёт')]")))  #  Поле ввода с надписью "Лицевой счет"
        assert 'Лицевой счёт' in field_personal_account.text  #  Проверка, что есть такое поле
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-login'))).click()  # Таб "Логин"
        Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys('testing123')  #  Зполняем поле "Логин", данные вымышлены
        field_login = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Логин')]"))) # Поле ввода с надписью "Логин"
        assert 'Логин' in field_login.text  #  Проверка, что есть такое поле
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-mail'))).click()  # Таб "Почта"
        Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys('den.gusev.test@mail.ru')  #  Зполняем поле "Электронная почта", данные актуальны
        field_mail = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Электронная почта')]")))  # Поле ввода с надписью "Электронная почта"
        assert 'Электронная почта' in field_mail.text  #  Проверка, что есть такое поле
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()  # Таб "Телефон"
        Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']"))).send_keys('89511111111')  #  Зполняем поле "Мобильный телефон", данные вымышлены
        field_mobile = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Мобильный телефон')]")))  # Поле ввода с надписью "Мобильный телефон"
        assert 'Мобильный телефон' in field_mobile.text  #  Проверка, что есть такое поле
        field_password = driver.find_element(By.XPATH, "//span[contains(text(),'Пароль')]")  #  Поле ввода с надписью пароль
        assert 'Пароль' in field_password.text  #  Проверка, что есть такое поле
        personal_cabinet_text = driver.find_element(By.XPATH, "//h2[contains(text(),'Личный кабинет')]")  #  Надпись на странице авторизации
        assert 'Личный кабинет' in personal_cabinet_text.text  #  Проверка, что есть такая надпись есть
        slogan = driver.find_element(By.XPATH, "//p[contains(text(),'Персональный помощник в цифровом мире Ростелекома')]")  #  Слоган
        assert 'Персональный помощник' in slogan.text  #  Проверка, что есть такая надпись есть

    """Тестирование ссылки на пользовательсое соглашение и возврат на страницу авторизации"""
    def test_terms_of_use(self, driver):  # Проверяем ссылку на пользовательское соглашение
        page = Page(driver)
        page.open()
        page.terms_of_use_open()
        driver.switch_to.window(driver.window_handles[1])
        terms_of_use_link = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//h1[@class="offer-title"]')))    # Пользовательское соглашение
        assert 'Публичная оферта' in terms_of_use_link.text
        driver.switch_to.window(driver.window_handles[0])
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  # Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование открытия формы регистрации и возврат на страницу авторизации"""
    def test_check_registration_form_can_open(self, driver):   # Проверяем открытие формы регистрации и возврат на страницу авторизации
        page = Page(driver)
        page.open()
        page.registration_form_open()
        registration_text_on_registration_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//h1[@class="card-container__title"]')))  #  Надпись "Регистрация" в форме регистрации
        assert 'Регистрация' in registration_text_on_registration_page.text
        driver.back()
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  # Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование ссылки ВК и возврат на страницу авторизации"""
    def test_vk_icon_open(self, driver):  # Проверяем открытие ссылки на соц сеть ВК и возврат на страницу авторизации
        page = Page(driver)
        page.open()
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#oidc_vk'))).click()  #  Иконка ВК
        rtk_passport = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@data-key="service"]')))  #  Текст на форме авторизации в ВК
        assert 'РТК Паспорт' in rtk_passport.text
        driver.back()
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  # Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование ссылки Одноклассники и возврат на страницу авторизации"""
    def test_ok_icon_open(self, driver):  #  Проверяем открытие ссылки на соц сеть Одноклассники и возврат на страницу авторизации
        page = Page(driver)
        page.open()
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#oidc_ok'))).click()  # Иконка Одноклассники
        label_odnoklassniki = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Одноклассники')]")))  #  Лэйбл Одноклассники
        assert 'Одноклассники' in label_odnoklassniki.text
        driver.back()
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  # Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование ссылки Почта и возврат на страницу авторизации"""
    def test_mail_icon_open(self, driver):  #  Проверяем открытие ссылки на соц сеть Mail и возврат на страницу авторизации
        page = Page(driver)
        page.open()
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#oidc_mail'))).click()  # Иконка Mail
        label_mail = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Мой Мир@Mail.Ru')]")))  # Лэйбл Mail
        assert 'Мой Мир' in label_mail.text
        driver.back()
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  # Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование ссылки Яндекс и возврат на страницу авторизации"""
    def test_ya_icon_open(self, driver): #  Проверяем открытие ссылки на соц сеть Ya и возврат на страницу авторизации
        page = Page(driver)
        page.open()
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#oidc_ya'))).click()  # Иконка Ya
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#oidc_ya'))).click()  # Повторное нажатие на иконку Ya, так как с первого раза не происходит переход на страницу
        label_ya = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Яндекс')]")))  # Лэйбл Ya
        assert 'Яндекс' in label_ya.text
        driver.back()
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  # Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование ссылки Забыл пароль и возврат на страницу авторизации"""
    def test_button_forget_password(self, driver):  # Проверяем открытие формы восстановления пароля и выход на форму авторизации
        page = Page(driver)
        page.open()
        page.forgot_password_form_open()  #Ссылка "Забыл пароль"
        forget_password_form = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")))  # Форма восстановления пароля
        assert 'Восстановление пароля' in forget_password_form.text
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#reset-back'))).click()  #  Выходим из формы восстановления пароля
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  #  Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text

    """Тестирование чекбокса Запомнить меня"""
    def test_checkbox(self, driver):  #  Проверяем чекбокс "Запомнить меня", можно ли убрать и установить галочку (по умолчанию галочка стоит)
        page = Page(driver)
        page.open()
        Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="rt-checkbox__label"]'))).click()  #  Убираем галочку чекбокса
        class_name_empty_checkbox = driver.find_element(By.CLASS_NAME, 'rt-checkbox').get_attribute('class')  #  Имя класса без галочки "rt-checkbox"
        Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="rt-checkbox__label"]'))).click()  #  Ставим галочку чекбокса
        class_name_full_checkbox = driver.find_element(By.XPATH, '//div[@class="rt-checkbox rt-checkbox--checked"]').get_attribute('class')  #  Имя класса с галочкой "rt-checkbox rt-checkbox--checked"
        assert  class_name_empty_checkbox != class_name_full_checkbox  #  Если имена классов не равны - галочка убирается и ставится

    """Тестрование регистрации на сайте с валидными данными"""
    def test_registration_on_site(self, driver):  #  Проверяем возможность регистрации на сайте
        page = Page(driver)
        page.open()
        page.registration_form_open()  #  Открываем форму регистрации
        page.registration_form_fill_fields_and_submit_with_valid_data()  #  Заполняем форму регистрации
        confirm_email = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Подтверждение email')]"))) #  Страница ввода кода для подтверждения email
        assert 'Подтверждение' in confirm_email.text  #  Проверяем, что присутствует надпись "Подтверждение email", значит регистрация должна пройти успешно
        driver.back()
        driver.back()  #  Необходимо 2 раза нажать на стрелочку возврата в браузере для возврата на страницу авторизации
        authorization_text_on_authorization_page = Wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Авторизация')]")))  # Страница авторизации
        assert 'Авторизация' in authorization_text_on_authorization_page.text  #  Проверяем, что произошел возврат на страницу авторизации


    """Тестирование поля Регион на ввод разных регионов"""
    def test_registration_field_region(self, driver):  # Проверка выпадающего списка Регион, возможно ли выбрать предлагаемый регион, по умолчанию Москва
        page = Page(driver)
        page.open()
        page.registration_form_open()
        Wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.rt-input__action svg.rt-base-icon.rt-base-icon--fill-path.rt-select__arrow"))).click()  # Нажимаем на стрелочку, чтобы появился выпадающий список
        drop_dawn_list = [i.text.split('\n') for i in (Wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="rt-select__list-wrapper rt-select__list-wrapper--rounded"]'))))][0]  # Выпадающий список
        drop_dawn_list.pop(0)  # Удаляем фразу "Выберите свой регион"
        random_region = random.choice(drop_dawn_list)  # Рандомный регион
        Wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.register-form__dropdown input.rt-input__input"))).send_keys(random_region)  # Вводим рандомный регион из списка возможных
        mouse.move(1005, 503, duration=0.1)  # Координаты мыши для навигации на выбранный регион
        mouse.click('left')  # Наводим мышку на введенный регион и кликаем
        driver.execute_script("document.getElementsByClassName('rt-input__mask')[2].style.display='inline'")  # Скрипт для видимости региона
        region = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(),'{random_region}')]")))  # Появившийся в поле ввода регион
        assert f'{random_region}' == region.text  # Если проверка проходит, значит регион ввести возможно, поле работает
        print(f'{region.text} = {random_region}')