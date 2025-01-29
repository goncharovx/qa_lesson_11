import os

import allure
from selene import browser, have
from selene.api import s

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'resources', 'pic.png')


def test_form_submission_with_s_and_banner_removal():
    with allure.step('Открыть форму регистрации'):
        browser.open('/automation-practice-form')

    with allure.step('Заполнить ФИО'):
        s('#firstName').type('Sonic')
        s('#lastName').type('Syndicate')

    with allure.step('Заполнить поле ввода e-mail'):
        s('#userEmail').type('test@mail.ru')

    with allure.step('Выбрать пол'):
        s('[for="gender-radio-1"]').click()  # Male

    with allure.step('Заполнить поле ввода телефон'):
        s('#userNumber').type('9939993388')

    with allure.step('Установить дату рождения'):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click().s('[value="2"]').click()
        s('.react-datepicker__year-select').click().s('[value="1960"]').click()
        s('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click()

    with allure.step('Выбрать предмет'):
        s('#subjectsInput').type('Maths').press_enter()

    with allure.step('Выбрать хобби'):
        s('[for="hobbies-checkbox-1"]').click()  # Sports
        s('[for="hobbies-checkbox-3"]').click()  # Music

    with allure.step('Загрузить файл'):
        s('#uploadPicture').send_keys(file_path)

    with allure.step('Заполнить поле ввода "адресс"'):
        s('#currentAddress').type('Moscow 5')

    with allure.step('Выбрать штат'):
        s('#state').click().s('#react-select-3-option-0').click()

    with allure.step('Выбрать город'):
        s('#city').click().s('#react-select-4-option-0').click()

    with allure.step('Подтвердить регистрацию'):
        s('#submit').click()

    with allure.step('Проверить форму регистрации'):
        s('.table-responsive').should(have.text('Sonic Syndicate'))
        s('.table-responsive').should(have.text('test@mail.ru'))
        s('.table-responsive').should(have.text('Male'))
        s('.table-responsive').should(have.text('9939993388'))
        s('.table-responsive').should(have.text('03 March,1960'))
        s('.table-responsive').should(have.text('Maths'))
        s('.table-responsive').should(have.text('Sports'))
        s('.table-responsive').should(have.text('Music'))
        s('.table-responsive').should(have.text('pic.png'))
        s('.table-responsive').should(have.text('Moscow 5'))
        s('.table-responsive').should(have.text('NCR Delhi'))
