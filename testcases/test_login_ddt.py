from selenium import webdriver
from pageobjects.home_page import page_homepage
from pageobjects.account_registration import page_acc_register
from pageobjects.account_login import page_acc_login
from utilities import XLUtility
from selenium.webdriver.common.by import By
import pytest
import time
from utilities import randomstring
from utilities.readproperties import readconfig
import logging
import os


class Test_Login_Ddt():
    baseURL = readconfig.get_url()  #saving the url
    path = os.path.abspath(os.pardir)+"\\testdata\\login_data.xlsx"     #path for excel file

    def test_login_ddt(self,setup):
        logging.info("**** Starting test_login_ddt *******")    #for logging

        #calls the method for row count
        self.rows=XLUtility.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = page_homepage(self.driver)  # HomePage Page Object Class
        self.reg = page_acc_register(self.driver)  # LoginPage Page Object Class
        self.lp = page_acc_login(self.driver)  # MyAccount Page Object class

        self.driver.implicitly_wait(30)     #implicit wait
        self.driver.refresh()
        time.sleep(30)

        #Loop for reading data from sheet1
        for r in range(2,self.rows+1):
            time.sleep(5)
            self.hp.myaccount_ck()
            time.sleep(60)
            self.hp.login_ck()
            time.sleep(5)
            self.email=XLUtility.readData(self.path,"Sheet1",r,1)
            self.password = XLUtility.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtility.readData(self.path, "Sheet1", r, 3)
            time.sleep(2)
            self.lp.set_email_id(self.email)    # sending the email as param.
            self.lp.set_password_id(self.password)  #sending the password as param
            self.lp.set_login_xpath()
            time.sleep(10)

            #try......except for exception handling
            try:
                if self.driver.find_element(By.XPATH, "//*[@id='content']/h2[1]").text == "My Account":
                    self.driver.save_screenshot(
                        os.path.join("C:\\Users\\usha5\\PycharmProjects\\Opencart_Project\\screenshots", "scrnshot.png"))
                self.targetpage=True
                print("true")
                time.sleep(40)
                if self.exp=='valid':
                    if self.targetpage==True:
                        lst_status.append('Pass')
                        self.hp.myaccount_ck()  #calls the method for myaccount
                        self.lp.set_logout_xpath()  #calls the method for logout
                        time.sleep(30)
                   # self.driver.close()
                    else:
                        lst_status.append('Fail')
                        time.sleep(30)
                elif self.exp=='invalid':
                    if self.targetpage == True:
                        lst_status.append('Fail')
                        self.hp.myaccount_ck()      #calls for Myaccount
                        self.lp.set_logout_xpath()  #calls logout method
                        time.sleep(30)
                    #self.driver.close()
            except:
                    lst_status.append('Pass')
                    time.sleep(40)
        self.driver.close()
        #final validation
        if "Fail" not in lst_status:
          assert True
        else:
          assert False
          # for logging info
          logging.info("******* End of test_003_login_Datadriven **********")
