import time
import random
from stringcolor import *

from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Errors:
    # Info
    x = 1


# Error Method
def geterrors(self):
    # Error Conditions
    GoogleDriveErr = "Unidentified Google Drive Path"
    GoogleFormLinkErr = "Invalid Google Form Link"

    # Error Handler
    if self == 1:
        print(GoogleDriveErr)

    elif self == 2:
        print(GoogleFormLinkErr)

    else:
        print(self)
