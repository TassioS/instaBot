import sys
sys.path.insert(0,'utils')
from elementTools import *
from loginObjects import *

def login(driver, username, password):
    sendText(username, usernameField(driver))
    sendText(password, passwordField(driver))
    clickElement(logInButton(driver))