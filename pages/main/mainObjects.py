
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils.elementTools import waitElement

def searchField(driver: WebDriver):
    return waitElement(driver, By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div')

def searchFieldInput(driver: WebDriver):
    return waitElement(driver, By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input[1]')
