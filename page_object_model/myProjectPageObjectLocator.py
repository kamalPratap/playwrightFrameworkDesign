import os
import time

from playwright.sync_api import Page


class MyProjectPOM:
    def __init__(self, page: Page):
        self.page = page
        self.plus_icon_on_myProjectPage = 'xpath=//*[@title="Add new content"]'
        self.upload_project = 'xpath=//*[@href="app?edit=true"]'
        self.choose_file = page.get_by_label("Project File")
        self.replace = page.get_by_label("Replace")
        self.upload_button = page.get_by_role("button", name="Upload")

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

    # def click_replace_checkbox(self):
    #     self.replace.check()
