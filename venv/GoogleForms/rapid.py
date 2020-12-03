import time
import random

from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import welcome
import errors


class Rapid:
    x = 1


def getrapid():
    # Chrome Driver
    try:
        chromedriver = "/usr/local/bin/chromedriver"
        driver = webdriver.Chrome(chromedriver)

    except:
        err = errors.geterrors(1)
        exit()

    # Target Form
    userlink = input("Enter Your Google Form Url: \n")
    verifiedlink = userlink.startswith("https://docs.google.com/forms/")

    try:
        link = userlink
        driver.get(userlink)
    except:
        if not verifiedlink:
            err = errors.geterrors(2)
            exit()

    # Target Option

    # Item One
    itemxpathone = input("Enter First Item XPath : \n")
    verifiedxpath = itemxpathone.startswith("//*[@id=")

    try:
        optionpath = itemxpathone

    except:
        if not verifiedxpath:
            err = errors.geterrors(3)
            exit()

    # Item Two
    itemxpathtwo = input("Enter Second Item XPath : \n")
    verifiedxpath = itemxpathtwo.startswith("//*[@id=")
    try:
        submitpath = itemxpathtwo
    except:
        if not verifiedxpath:
            err = errors.geterrors(3)
            exit()

    # Counter
    rapidamount = int(input("Enter The Amount of Operations: "))
    counter = 0

    while counter < rapidamount:
        # Choice Automation
        choice = driver.find_element_by_xpath(optionpath)
        webdriver.ActionChains(driver).move_to_element(choice).click(choice).perform()
        time.sleep(0.5)

        # Submit Automation
        submit = driver.find_element_by_xpath(submitpath)
        webdriver.ActionChains(driver).move_to_element(submit).click(submit).perform()

        # Counter & Redo
        counter = counter + 1
        driver.get(userlink)
