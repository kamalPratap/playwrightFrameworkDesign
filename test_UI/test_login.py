import time
import pytest

from page_object_model.login_logout import LoginLogoutPage
from page_object_model.myProjectPageObjectLocator import MyProjectPOM


#@pytest.mark.regression
def test_run(login_set_up):
    page = login_set_up
    lp1 = LoginLogoutPage(page)
    lp1.login()
    time.sleep(1)
    prj = MyProjectPOM(page)
    prj.add_project()
    prj.click_replace_checkbox()
    time.sleep(5)
    lp1.logout()


# @pytest.mark.skip(reason="not ready")
# def test_run_v1(login_set_up):
#     page = login_set_up
#     lp1 = LoginLogoutPage(page)
#     lp1.login()
#     time.sleep(1)
#     lp1.logout()
#
#
# @pytest.mark.xfail(reason="URL not ready")
# def test_run_v2(login_set_up):
#     page = login_set_up
#     lp1 = LoginLogoutPage(page)
#     lp1.login()
#     time.sleep(1)
#     lp1.logout()
