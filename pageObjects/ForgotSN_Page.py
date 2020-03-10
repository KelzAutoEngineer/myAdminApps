class ForgotSN():
    textbox_surname_id = "surname"
    textbox_names_id = "firstNames"
    dropdown_DOB_xpath = "/html/body/div/unisa-root/unisa-forgot-student-search/div/form/div[3]/div/div/input"
    click_dropdown_xpath = "/html/body/div/unisa-root/unisa-forgot-student-search/div/form/div[3]/div/div/span/button/span"
    select_radioBtn_xpath = "/html/body/div/unisa-root/unisa-forgot-student-search/div/form/div[4]/label/input"
    textbox_idNumber_id = "identityNumber"
    select_radioBtn2_xpath = "/html/body/div/unisa-root/unisa-forgot-student-search/div/form/div[6]/label/input"
    textbox_passportNum_id = "passportNumber"
    submit_btn_xpath = "/html/body/div/unisa-root/unisa-forgot-student-search/div/form/div[7]/button"
    back_btn_xpath = "/html/body/div/unisa-root/unisa-forgot-student-result/div/div[3]/div/button"

    def __init__(self, driver):
        self.driver = driver

    def addSurname(self, id_surname):
        self.driver.find_element_by_id(self.textbox_surname_id).send_keys("Ming Sun")

    def addFullNames(self, id_names):
        self.driver.find_element_by_id(self.textbox_names_id).send_keys("Jason")

    def selectDOB(self, id_dob):
        self.driver.find_element_by_xpath(self.dropdown_DOB_xpath).send_keys("1975-05-06")

    def clickDrop(self):
        self.driver.find_element_by_xpath(self.click_dropdown_xpath).click()

    def selectRadio1(self):
        self.driver.find_element_by_xpath(self.select_radioBtn_xpath).click()

    def addID_Number(self):
        self.driver.find_element_by_id(self.textbox_idNumber_id).send_keys()

    def selectRadio2(self):
        self.driver.find_element_by_xpath(self.select_radioBtn2_xpath).click()

    def addPassport_Number(self):
        self.driver.find_element_by_id(self.textbox_passportNum_id).send_keys()

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.submit_btn_xpath).click()

    def clickBack(self):
        self.driver.find_element_by_xpath(self.back_btn_xpath).click()