import os
import time

from playwright.sync_api import Page

from page_object_model.myProjectPageObjectLocator import MyProjectPOM


class LoginLogoutPage(MyProjectPOM):
    def __init__(self, page: Page):
        super().__init__(page)
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

    def add_project(self):
        self.page.click(self.plus_icon_on_myProjectPage)
        time.sleep(1)
        self.page.click(self.upload_project)
        current_working_dir = os.getcwd()
        file_path = os.path.join(current_working_dir, "input_data", "playwright_project_project.zip")
        time.sleep(1)
        self.choose_file.set_input_files(file_path)
        time.sleep(1)
        self.replace.click()
        self.upload_button.click()
        #page.get_by_label("Project File").set_input_files(file_path)