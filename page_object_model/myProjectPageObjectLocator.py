from playwright.sync_api import Page


class MyProjectPOM:
    def __init__(self, page: Page):
        self.page = page
        self.plus_icon_on_myProjectPage = 'xpath=//*[@title="Add new content"]'
        self.upload_project = 'xpath=//*[@href="app?edit=true"]'
        self.choose_file = page.get_by_label("Project File")
        self.replace = page.get_by_label("Replace")
        self.upload_button = page.get_by_role("button", name="Upload")



    # def click_replace_checkbox(self):
    #     self.replace.check()
