from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class page_acc_register():

    first_name = "firstname"
    last_name = "lastname"
    email_name = "email"
    password_name = "password"
    subscribe_id = "input-newsletter"
    continue_xpath = "//*[@id='form-register']/div/button"
    privacy_name="agree"


    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self,fname):
        self.driver.find_element(By.NAME,self.first_name).send_keys(fname)

    def set_last_name(self,lname):
        #self.driver.find_element(By.NAME(self.last_name)).clear()
        self.driver.find_element(By.NAME,self.last_name).send_keys(lname)

    def set_email_name(self, ename):
        #self.driver.find_element(By.NAME(self.email_name)).clear()
        self.driver.find_element(By.NAME,self.email_name).send_keys(ename)

    def set_password_name(self, pword: object) -> object:
        #self.driver.find_element(By.NAME(self.password_name)).clear()
        self.driver.find_element(By.NAME,self.password_name).send_keys(pword)

    def set_subscribe_id(self):
    #    self.driver.find_element(By.XPATH(self.email_name)).clear()
        self.driver.find_element(By.ID,self.subscribe_id).click()

    def set_privacy_name(self):
        self.driver.find_element(By.NAME,self.privacy_name).click()


    def set_continue_xpath(self):
        self.driver.find_element(By.XPATH,self.continue_xpath).click()



