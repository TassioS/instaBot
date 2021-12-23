import sys
from utils.elementTools import clickElement
from utils.elementTools import sendText, clickElement
from pages.login.loginObjects import *

def login(driver, username, password):
    sendText(username, usernameField(driver))
    sendText(password, passwordField(driver))
    clickElement(logInButton(driver))
    clickElement(notNowLoginInfoButton(driver))
    clickElement(notNowNotificationsButton(driver))