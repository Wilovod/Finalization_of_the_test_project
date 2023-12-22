from testpage import OperationsHelper
import logging
import yaml
import time

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 Starting")
    test_page_1 = OperationsHelper(browser)
    test_page_1.go_to_site()
    test_page_1.enter_login("test")
    test_page_1.enter_pass("test")
    test_page_1.click_login_button()
    assert test_page_1.get_error_text() == "401"


def test_step_2(browser):
    logging.info("Test2 starting")
    test_page_2 = OperationsHelper(browser)
    test_page_2.go_to_site()
    time.sleep(1)
    test_page_2.enter_login("GB2023070359817")
    test_page_2.enter_pass("6dd73090c5")
    time.sleep(1)
    test_page_2.click_login_button()
    test_page_2.Contact_click()
    time.sleep(2)
    test_page_2.enter_name("Dmitriy")
    test_page_2.enter_email("kds360@mail.ru")
    test_page_2.enter_text("Text")
    time.sleep(2)
    test_page_2.click_contact_us()
    time.sleep(1)
    assert test_page_2.get_alert_message() == "Form successfully submitted", "test FAILED"
