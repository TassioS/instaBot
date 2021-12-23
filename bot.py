from pages.main.mainFactory import openPage
from selenium import webdriver
from json import load
from pages.login.loginFactory import login

data = load(open('config.json'))

driver = webdriver.Chrome(data['chromeDriverPath'])
driver.get("https://www.instagram.com/")


login(driver, data['username'], data['password'])
for page in data['pages']:
    openPage(driver, page)

#driver.quit()