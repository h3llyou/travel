# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CitilinkLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://book.citilink.co.id/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_citilink_login(self):
        driver = self.driver
        driver.get(self.base_url + "/loginagency.aspx")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=Subang | ]]
        driver.find_element_by_link_text("Login").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=Subang | ]]
        driver.find_element_by_id("ControlGroupLoginAgencyView_AgentLoginLoginAgencyView_PasswordFieldPassword").clear()
        driver.find_element_by_id("ControlGroupLoginAgencyView_AgentLoginLoginAgencyView_PasswordFieldPassword").send_keys("0038000423")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=Subang | ]]
        driver.find_element_by_id("ControlGroupLoginAgencyView_AgentLoginLoginAgencyView_PasswordFieldPassword").clear()
        driver.find_element_by_id("ControlGroupLoginAgencyView_AgentLoginLoginAgencyView_PasswordFieldPassword").send_keys("LiNeLuCNCt!1")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=Subang | ]]
        driver.find_element_by_id("ControlGroupLoginAgencyView_AgentLoginLoginAgencyView_ButtonLogIn").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
