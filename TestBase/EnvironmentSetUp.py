import unittest

from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):
    baseURL = "https://myadminqa.int.unisa.ac.za/services/forgot-studentnumber-app/"
    driver = webdriver.Firefox

    #  setUp contains the browser setup attributes
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    #  tearDown method is used to close all the browser instances and then quit
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()