from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.home_page import page_homepage
from pageobjects.account_registration import page_acc_register
import pytest
import time
import os
from utilities import randomstring
from utilities.readproperties import readconfig
import logging

class Test_homepage():
    burl = readconfig.get_url()         #saving the url from the config file
    def test_homepage(self,setup):
        self.driver = setup             #set up the chrome driver
        logging.getLogger('Test').info('****Testing Started****')   #for logging
        self.driver.get(self.burl)
        self.driver.maximize_window()
        #time.sleep(30)
        self.hp = page_homepage(self.driver)    #object creation for the page_homepage
        self.driver.implicitly_wait(30)         #implicit wait
        self.driver.refresh()
        #time.sleep(30)
        self.hp.myaccount_ck()          #calls method to click myaccount
        time.sleep(5)
        self.hp.register_ck()           #calls method to click register
        #self.driver.save_screenshot("reg_page.png")
        self.accp= page_acc_register(self.driver)   #object creation for page_acc_register
        logging.getLogger('Test').debug('****Testing is going on ******')   #for logging

        #calls the appropriate methods for giving the account details...

        self.accp.set_first_name('abc')
        self.accp.set_last_name('xyz')
        email_name = randomstring.generate_random_string()+"@gmail.com"
        self.accp.set_email_name(email_name)
        self.p_word = readconfig.get_password()
        self.accp.set_password_name(self.p_word)

        self.driver.save_screenshot(os.path.join("C:\\Users\\usha5\\Downloads\\OpencartProject\\screenshots","scrshot.png"))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(20)

        self.accp.set_subscribe_id()
        self.accp.set_privacy_name()
        self.accp.set_continue_xpath()
        time.sleep(3)

        logging.getLogger('Test').info('****Testing Finished ******')   #for logging
        #self.driver.execute_script("window.scrollTo(0, 0);")

        #checks the account page
        if self.driver.find_element(By.XPATH,"//*[@id='content']/h1") == "Your Account Has Been Created!":
           self.driver.save_screenshot(os.path.join("C:\\Users\\usha5\\PycharmProjects\\Opencart_Project\\screenshots","scrnshot.png"))
           assert True
        else:
           self.driver.save_screenshot(os.path.join("C:\\Users\\usha5\\PycharmProjects\\Opencart_Project\\screenshots","scrnshot.png"))
           self.driver.close()




