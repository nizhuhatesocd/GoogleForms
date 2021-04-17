import time
import random

import html
import requests
from sty import fg, bg, ef
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import welcome
import errors


class Rapid:

    chromedriver = None

def getrapid():
    # Chrome Driver
    print(fg(252, 245, 38) + "[*] After Entering The Path We Will Save The Data !")
    print(fg(252, 245, 38) + "[*] You Can Download Chrome Driver From https://chromedriver.chromium.org/downloads")
    chromedriver = (input(fg(79, 176, 140) + "[~] Please Enter Your Driver Path : "))

    try:
        chromedriverValidated = chromedriver.endswith("chromedriver")
        driver = webdriver.Chrome(chromedriver)
    except:
        if not chromedriverValidated:
            err = errors.geterrors(1)
            exit()

    # Target Form
    userlink = input(fg(79, 176, 140) + "[~] Enter Your Google Form Url: ")
    verifiedlink = userlink.startswith("https://docs.google.com/forms/")

    try:
        link = userlink
        driver.get(userlink)
    except:
        if not verifiedlink:
            err = errors.geterrors(2)
            exit()

    # Target Options
    req = requests.get(userlink)
    soup = BeautifulSoup(req.content, "html.parser")

    print("Recognizing Answers ... \n \n")
    print(fg(0, 255, 145) + "[?] Which One Is Your Target ? \n")

    optioncount = 0
    alloptions = ["Please Select From Available Targets"]

    for options in soup.find_all("span", class_="freebirdFormviewerComponentsQuestionRadioLabel") or soup.find_all("span", class_="freebirdFormviewerComponentsQuestionCheckboxLabel"):
        optioncount = optioncount + 1
        convertcount = str(optioncount)
        print(convertcount + ". " + options.text)
        alloptions.append(options.text)
    
    
    # User Target
    usertarget = input("\nEnter Your Target [1 TO {max}] : ".format(max = convertcount))
    converttarget = int(usertarget)

    if converttarget > 0 :
        print("Performing Attack On {0} ...".format(alloptions[converttarget]))
        allcheckboxes = []
        for checkboxes in soup.find_all("span", class_="exportInnerBox"):
            checkboxcount = checkboxcount + 1
            convertcount = str(checkboxcount)
            allcheckboxes.append(checkboxes)
        print("Found {0} Checkboxes !".format(convertcount))

    else:
        print(fg(255, 76, 36) + "Invalid Menu Number !")
        

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
