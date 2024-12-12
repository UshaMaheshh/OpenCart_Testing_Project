from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pageobjects.home_page import page_homepage
from pageobjects.account_login import page_acc_login
from selenium.webdriver.common.by import By
import pytest
import time
import logging
from utilities.readproperties import readconfig

class Test_account_login():
    burl = readconfig.get_url()         #getting the url from the config file
    def test_homepage(self,setup):
        self.driver=setup               #set up the chrome driver
        self.driver.get(self.burl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30) #implicit wait
        self.hp = page_homepage(self.driver)    #object creation for page_homepage
        self.driver.refresh()
        #time.sleep(60)
        self.hp.myaccount_ck()      #calls the method for Myaccount
        time.sleep(2)
        self.hp.login_ck()          #for Login
        # self.driver.save_screenshot("reg_page.png")
        self.accp = page_acc_login(self.driver)
        # for logging
        logging.getLogger('Test').info('******Testing*****is*****going on******')
        time.sleep(2)
        self.acc_lp= page_acc_login(self.driver)    #object creation for page_acc_login

        #assigning the mail and password for parameters

        self.acc_lp.eid="yiyi123@gmail.com"
        self.acc_lp.pid="1234y"

        self.acc_lp.set_email_id(self.acc_lp.eid)
        self.acc_lp.set_password_id(self.acc_lp.pid)
        self.acc_lp.set_login_xpath()
        time.sleep(6)

        #try...except...finally for exception handling
        try:
            self.element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Account"))
                )
            if self.element.text=="Account":
               print(self.element.text)
               assert True

        except TimeoutException:    #for TimeoutException
            print("Timeout reached. The element was not found within 60 seconds.")
            # Close the browser if the element is not found
        finally:
            self.driver.close()






