import time
import unittest

from appium import webdriver
from selenium import webdriver


class BaseSetUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_cap = {
            "udid": "emulator-5554",
            "platformVersion": "7.1.2",
            "platformName": "Android",
            "appPackage": "com.todoist",
            "appActivity": "com.todoist.activity.HomeActivity"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print("Test complete")
