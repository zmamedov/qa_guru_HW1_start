from selene import browser, be, have


browser.open('https://ya.ru')
browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[class="Button2 Button2_pin_circle-circle Button2_size_l '
                'Distribution-SplashScreenModalCloseButtonOuter"]').click()
browser.element('[accesskey="1"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
