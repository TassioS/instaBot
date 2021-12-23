
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from pages.main.mainObjects import searchField, searchFieldInput
from utils.elementTools import clickElement, sendText


def openPage(driver: WebDriver, pageName):
    clickElement(searchField(driver))
    sendText(pageName, searchFieldInput(driver))
    sendText(Keys.ENTER, searchFieldInput(driver))
    sendText(Keys.ENTER, searchFieldInput(driver))
    