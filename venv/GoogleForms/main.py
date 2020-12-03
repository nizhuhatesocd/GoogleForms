import time
import random

from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import welcome
import rapid


class Main:
    # Banner
    banner = welcome.getwelcome()
    selectedmenu = int(input("Select From [1 TO 3]: \n"))

    # Menu Splitter
    
    # Rapid Input
    if selectedmenu == 1:
        print("Started the Rapid Operation ...")
        rapidattack = rapid.getrapid()

    # Secret Finder
    elif selectedmenu == 2:
        print("Started the Answer Attack")

    # Exit GoogleForms Hack
    elif selectedmenu == 3:
        print("The Program Will Exit ...")
        exit()

    # Unknown Credential
    else:
        print("Unknown Menu Value !")
        exit()
