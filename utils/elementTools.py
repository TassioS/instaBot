import random
import time
from typing_extensions import Literal
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def waitElement(driver: WebDriver, locator: Literal, elementValue: str):
	timeOut = 3
	try:
		return WebDriverWait(driver, timeOut).until(EC.presence_of_element_located((locator,elementValue)))
	except:
		print('Loading took too much time!')
	finally:
		print('Element is ready!')
  
def clickElement(element):
    delayAction()
    element.click()    

def sendText(text: str, element):
    delayAction()
    element.send_keys(text)
    

def delayAction(delay: float = 2):
    delay = random.uniform(0.5,delay)
    print(f'Action delayed by {delay}')
    time.sleep(delay)
