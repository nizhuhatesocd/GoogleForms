import time
import random
from stringcolor import *

from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Welcome:
    # Colors
    Green = '\033[32m'
    Blue = '\033[34m'
    Magenta = '\033[35m'
    Cyan = '\033[36m'
    LightGray = '\033[37m'
    DarkGray = '\033[90m'
    LightGreen = '\033[92m'
    LightYellow = '\033[93m'
    LightBlue = '\033[94m'
    LightMagenta = '\033[95m'
    LightCyan = '\033[96m'
    White = '\033[97m'


# Banner
def getwelcome():
    LightRed = '\033[91m'
    banner = 'Google Forms'
    figlet = Figlet(font='slant')
    print(
        '\n                 |================|                              '
        '\n                 | I Hate         |                              '
        '\n ===========     |        Robots! |     ========                 '
        '\n ===========    /|================|     ==                       '
        '\n ===           /               =        ==                    ==='
        '\n ===          /                =        =====                 =  '
        '\n ===    =====   ==== ==== ==== = ====   =====  ==== = = =     ==='
        '\n =====     ==   =  = =  = =  = = ==     ==     =  = ==  =====   ='
        '\n ============   ==== ==== ==== = ====   ==     ==== =   = = = ==='
        '\n                             =                                   '
        '\n                          ====                                   '
    )

    print('\n \nWelcome To GoogleForms Hack \n \n [1] Rapid Input \n [2] Secret Finder \n [3] Exit \n \n'
          'Version 1.0.0 \n'
          'Developed By Ashkan Ebtekari\n'
          '2020 @ Copyright\n \n \n')
