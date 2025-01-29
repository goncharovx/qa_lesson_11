import os

from selene import browser, have
from selene.api import s

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'resources', 'pic.png')


def test_form_submission_with_s_and_banner_removal():
    browser.open('/automation-practice-form')

    s('#firstName').type('Sonic')
    s('#lastName').type('Syndicate')
    s('#userEmail').type('test@mail.ru')
    s('[for="gender-radio-1"]').click()  # Male
    s('#userNumber').type('9939993388')

    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click().s('[value="2"]').click()  # Март (03)
    s('.react-datepicker__year-select').click().s('[value="1960"]').click()  # 1960
    s('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click()  # 03

    s('#subjectsInput').type('Maths').press_enter()

    s('[for="hobbies-checkbox-1"]').click()  # Sports
    s('[for="hobbies-checkbox-3"]').click()  # Music

    s('#uploadPicture').send_keys(file_path)

    s('#currentAddress').type('Moscow 5')

    s('#state').click().s('#react-select-3-option-0').click()  # NCR
    s('#city').click().s('#react-select-4-option-0').click()  # Delhi

    s('#submit').click()

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
