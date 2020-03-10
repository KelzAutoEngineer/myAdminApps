from pageObjects.ForgotSN_Page import ForgotSN
from TestBase.EnvironmentSetUp import EnvironmentSetup
from selenium import webdriver
import time


class ForgotSNTest(EnvironmentSetup):
    driver = webdriver.Firefox(
        executable_path=r"C:\Users\tmaimakm\Documents\Gerko\geckodriver.exe")
    surname = "id_surname"
    names = "id_names"
    dob = "id_dob"

    def test_forgot(self):
        lp = ForgotSN(self.driver)
        lp.addSurname(self.surname)
        lp.addFullNames(self.names)
        lp.selectDOB(self.dob)
        lp.clickDrop()
        lp.clickSubmit()
        time.sleep(10)
        lp.clickBack()
