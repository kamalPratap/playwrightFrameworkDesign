import time

from playwright.sync_api import Page

from configs import config_file


class LoginLogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input_selector = "#username"
        self.password_input_selector = "#password"
        self.login_button_role = "#login-button"
        self.login_button_role = "#login-button"
        self.user_icon_selector = "#user-menu"
        self.logout_button_role = 'xpath=//*[@href="/frevvo/web/logout"]'

    def enter_username(self):
        self.page.fill(self.username_input_selector, "kamal@qafrevvo")

    def enter_password(self):
        self.page.fill(self.password_input_selector, "qafrevvo")

    def login_button(self):
        self.page.click(self.login_button_role)

    def user_icon(self):
        self.page.click(self.user_icon_selector)

    def logout_button(self):
        self.page.click(self.logout_button_role)

    def login(self, url_key=None):
        # self.navigate(url_key)
        self.enter_username()
        self.enter_password()
        self.login_button()

    def logout(self):
        self.user_icon()
        time.sleep(1)
        self.logout_button()
