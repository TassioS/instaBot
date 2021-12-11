import sys
from selenium import webdriver
from json import load
sys.path.insert(0,'utils')
sys.path.insert(1,'pages/login')
from loginFactory import login
from elementTools import *
from loginObjects import *

data = load(open('config.json'))

driver = webdriver.Chrome(data['chromeDriverPath'])
driver.get("https://www.instagram.com/")


login(driver, data['username'], data['password'])
driver.quit()