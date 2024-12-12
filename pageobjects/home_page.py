from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class page_homepage():

    my_account_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/a/i[1]"
    register_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a"
    acc_login_xpath = "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[2]/a"

    def __init__(self, driver):
        self.driver = driver
    def myaccount_ck(self):
        self.driver.find_element(By.XPATH,self.my_account_xpath).click()
    def register_ck(self):
        self.driver.find_element(By.XPATH,self.register_xpath).click()

    def login_ck(self):
        self.driver.find_element(By.XPATH,self.acc_login_xpath).click()
