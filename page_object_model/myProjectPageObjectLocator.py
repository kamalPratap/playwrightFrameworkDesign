from playwright.sync_api import Page


class MyProjectPOM:
    def __init__(self, page: Page):
        self.page = page
        self.plus_icon_on_myProjectPage = 'xpath=//*[@title="Add new content"]'
        self.replace = page.get_by_label("Replace")

    def add_project(self):
        self.page.click(self.plus_icon_on_myProjectPage)

    def click_replace_checkbox(self):
        self.replace.check()




# page.get_by_title("Add new content").click()
#     page.get_by_role("link", name=" Upload project").click()
#     page.get_by_label("Project File").click()
#     page.get_by_label("Project File").set_input_files("GeoLocation_form.zip")
#     page.get_by_label("Replace").check()
#     page.get_by_role("button", name="Upload").click()