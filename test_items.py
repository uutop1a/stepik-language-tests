"""Check the add-to-basket button on a product page."""

from selenium.webdriver.common.by import By


def test_guest_can_see_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    buttons = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")
    assert len(buttons) == 1 and buttons[0].is_displayed(), "Add-to-basket button is missing"
