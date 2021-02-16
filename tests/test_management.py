from selene import have
from selene.support.shared import browser


def test_basic_case():
    browser.open("http://todomvc4tasj.herokuapp.com/")
    browser.should(have.js_returned
                   (True, "return $._data($('#clear-completed')[0],'events').hasOwnProperty('click')"))

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list>li').element_by(have.exact_text('a')).double_click()
    browser.element('.editing').element('.edit').type(' edited').press_enter()

    browser.all('#todo-list>li').element_by(have.exact_text('a edited')).hover()\
        .element('.destroy').click()
    browser.all('#todo-list>li').should(have.exact_texts('b', 'c'))

    browser.all('#todo-list>li').element_by(have.exact_text('c')).double_click()
    browser.element('.editing').element('.edit').type(' to be canceled').press_escape()

    browser.all('#todo-list>li').element_by(have.exact_text('c')).element('.toggle').click()
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_text('b'))
