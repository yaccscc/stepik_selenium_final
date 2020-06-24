from .pages.main_page import MainPage


def test_quest_should_see_login_link(browser):
    page = MainPage("http://selenium1py.pythonanywhere.com/", browser)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage("http://selenium1py.pythonanywhere.com/", browser)
    page.open()
    page.go_to_login_page()
