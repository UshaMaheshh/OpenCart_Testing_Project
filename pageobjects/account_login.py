from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class page_acc_login():

    email_id = "input-email"
    password_id = "input-password"
    login_xpath = "//*[@id='form-login']/div[3]/button"
    logout_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[5]/a"

    def __init__(self, driver):
        self.driver = driver

    def set_email_id(self,eid):
        self.driver.find_element(By.ID,self.email_id).send_keys(eid)

    def set_password_id(self,pid):
        #self.driver.find_element(By.NAME(self.last_name)).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(pid)


    def set_login_xpath(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()

    def set_logout_xpath(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

