import time
import pytest

from page_object_model.login_logout import LoginLogoutPage


#@pytest.mark.regression
def test_run(login_set_up):
    page = login_set_up
    login_page = LoginLogoutPage(page)
    login_page.login()
    time.sleep(1)
    login_page.add_project()
    # prj.click_replace_checkbox()
    time.sleep(5)
    login_page.logout()


@pytest.mark.skip(reason="not ready")
def test_run_v1(login_set_up):
    page = login_set_up
    login_page = LoginLogoutPage(page)
    login_page.login()
    time.sleep(1)
    login_page.logout()


@pytest.mark.xfail(reason="URL not ready")
def test_run_v2(login_set_up):
    page = login_set_up
    login_page = LoginLogoutPage(page)
    login_page.login()
    time.sleep(1)
    login_page.logout()
