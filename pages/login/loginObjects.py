from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils.elementTools import waitElement

def usernameField(driver: WebDriver):
    return waitElement(driver, By.NAME, 'username')

def passwordField(driver: WebDriver):
    return waitElement(driver, By.NAME, 'password')

def logInButton(driver: WebDriver):
    return waitElement(driver, By.XPATH, '//*[@id="loginForm"]/div/div[3]')

def notNowLoginInfoButton(driver: WebDriver):
    return waitElement(driver, By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
    
def notNowNotificationsButton(driver: WebDriver):
    return waitElement(driver, By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')