import pytest
from playwright.sync_api import Playwright
from configs import config_file


# @pytest.fixture
# def set_up_browser_maximize(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
#     page = browser.new_page(no_viewport=True)
#     page.goto(config_file.URL)
#     yield page
#     page.close()
#
#
# @pytest.fixture
# def login_set_up(set_up_browser_maximize):
#     page = set_up_browser_maximize
#     # page.goto(config_file.URL)
#     yield page

@pytest.fixture
def set_up(page):
    page.goto(config_file.URL)
    yield page
    page.close()


@pytest.fixture
def login_set_up(set_up):
    page = set_up
    # page.goto(config_file.URL)
    yield page
