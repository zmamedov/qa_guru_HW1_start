from selene import browser, be, have


browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.all('[data-result="snippet"]').first.should(have.text('Selene - User-oriented Web UI browser tests in Python'))
