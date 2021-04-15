import time
import random

from sty import fg, bg, ef
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Errors:
    # Info
    GoogleDriveErr = None
    GoogleFormLinkErr = None


# Error Method
def geterrors(self):
    # Error Conditions
    GoogleDriveErr = "[!] Unidentified Google Drive Path !"
    GoogleFormLinkErr = "[!] Invalid Google Form Link !"

    # Error Handler
    if self == 1:
        print(fg(255, 76, 36) + GoogleDriveErr)

    elif self == 2:
        print(fg(255, 76, 36) + GoogleFormLinkErr)

    else:
        print(fg(255, 76, 36) + self)
