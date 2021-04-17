import time
import random

from sty import fg, bg, ef
from selectmenu import SelectMenu
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import welcome
import rapid


class Main:
    # Banner
    banner = welcome.getwelcome()

    # Menu Splitter
    menu = SelectMenu()
    menu.add_choices(["[1] Rapid Input", "[2] Secret Finder", "[3] Exit"])
    selected = 0
    result = menu.select("[?] What Type Of Attack You Want To Perform ?")

    if result == "[1] Rapid Input":
        selected = 1
        print("Starting Rapid Input Attack ...")
    elif result == "[2] Secret Finder":
        selected = 2
        print("This Tool is In Demo Build \n You Can Only Use Rapid Input Attack")
    elif result == "[3] Exit":
        selected = 3
        print("Exiting Program ...")
    
    # Rapid Input
    if selected == 1:
        print("Started the Rapid Operation ... \n")
        rapidattack = rapid.getrapid()

    # Secret Finder
    elif selected == 2:
        print("Started the Answer Attack ... \n")

    # Exit GoogleForms Hack
    elif selected == 3:
        print("The Program Will Exit ... \n")
        exit()

    # Unknown Credential
    else:
        print("Unknown Menu Value !")
        exit()
