import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    cur_lang = browser.execute_script("return window.navigator.language || window.navigator.userLanguage")
    if "fr" in cur_lang:
        time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")