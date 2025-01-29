import os
import allure
from selene import browser, have
from selene.api import s
from utils import attach

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'resources', 'pic.png')


@allure.step('Открыть форму регистрации')
def open_registration_form():
    browser.open('/automation-practice-form')
    attach.add_screenshot(browser)


@allure.step('Заполнить ФИО')
def fill_full_name():
    s('#firstName').type('Sonic')
    s('#lastName').type('Syndicate')


@allure.step('Заполнить поле ввода e-mail')
def fill_email():
    s('#userEmail').type('test@mail.ru')


@allure.step('Выбрать пол')
def select_gender():
    s('[for="gender-radio-1"]').click()


@allure.step('Заполнить поле ввода телефон')
def fill_phone():
    s('#userNumber').type('9939993388')


@allure.step('Установить дату рождения')
def set_date_of_birth():
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click().s('[value="2"]').click()
    s('.react-datepicker__year-select').click().s('[value="1960"]').click()
    s('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click()


@allure.step('Выбрать предмет')
def select_subject():
    s('#subjectsInput').type('Maths').press_enter()


@allure.step('Выбрать хобби')
def select_hobbies():
    s('[for="hobbies-checkbox-1"]').click()
    s('[for="hobbies-checkbox-3"]').click()


@allure.step('Загрузить файл')
def upload_file():
    s('#uploadPicture').send_keys(file_path)
    attach.add_screenshot(browser)


@allure.step('Заполнить поле ввода "адрес"')
def fill_address():
    s('#currentAddress').type('Moscow 5')


@allure.step('Выбрать штат')
def select_state():
    s('#state').click().s('#react-select-3-option-0').click()


@allure.step('Выбрать город')
def select_city():
    s('#city').click().s('#react-select-4-option-0').click()


@allure.step('Подтвердить регистрацию')
def submit_form():
    s('#submit').click()
    attach.add_screenshot(browser)
    attach.add_html(browser)


@allure.step('Проверить форму регистрации')
def verify_registration():
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
    attach.add_screenshot(browser)


def test_registration_form():
    open_registration_form()
    fill_full_name()
    fill_email()
    select_gender()
    fill_phone()
    set_date_of_birth()
    select_subject()
    select_hobbies()
    upload_file()
    fill_address()
    select_state()
    select_city()
    submit_form()
    verify_registration()