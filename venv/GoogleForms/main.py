import time
import random

from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import welcome


class Main:


    # Banner
    banner = welcome.getwelcome()
    selectedmenu = int(input("Select From [1 TO 3]: \n"))


    # Menu Splitter
    if selectedmenu == 1:
        print("Started the Rapid Operation ...")

    elif selectedmenu == 2:
        print("Started the Answer Attack")
    elif selectedmenu == 3:
        print("The Program Will Exit ...")
    else:
        print("Unknown Menu Value !")
        exit()
    

    # Chrome Driver
    chromedriver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chromedriver)

    # Target Form
    link = "https://docs.google.com/forms/d/e/1FAIpQLSfoe4on0CEB0ilWeSd5cM2wqTH2yO9CDOPSA3IeW0uGVfwXUw/viewform?usp=sf_link"
    driver.get(link)

    # Target Option
    optionpath = '//*[@id="i20"]/div[3]/div'
    submitpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span'

    # Counter
    counter = 0

    while counter < 100:
        # Choice Automation
        choice = driver.find_element_by_xpath(optionpath)
        webdriver.ActionChains(driver).move_to_element(choice).click(choice).perform()
        time.sleep(0.5)

        # Submit Automation
        submit = driver.find_element_by_xpath(submitpath)
        webdriver.ActionChains(driver).move_to_element(submit).click(submit).perform()

        # Counter & Redo
        counter = counter + 1
        driver.get(link)
