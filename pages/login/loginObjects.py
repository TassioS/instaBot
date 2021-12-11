import sys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
sys.path.insert(0,'utils')
from elementTools import waitElement

def usernameField(driver: WebDriver):
    return waitElement(driver, By.NAME, 'username')

def passwordField(driver: WebDriver):
    return waitElement(driver, By.NAME, 'password')

def logInButton(driver: WebDriver):
    return waitElement(driver, By.XPATH, '//*[@id="loginForm"]/div/div[3]')