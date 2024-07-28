from selene import browser, be, have


browser.open('https://ya.ru')
browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[type=button][class~=Button2_pin_circle-circle]').click()
browser.element('[accesskey="1"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
