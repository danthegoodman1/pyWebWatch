#! /usr/bin/env python

"""
Made with ❤ By Dan Goodman
"""

# Imports
import sys
import watcher
from os.path import expanduser

homeDir = expanduser("~")

configFile = {
    'darwin': '{}/.pyWebWatch/config.json'.format(homeDir),
    'linux': '{}/.pyWebWatch/config.json'.format(homeDir),
    'linux2': '{}/.pyWebWatch/config.json'.format(homeDir),
    'win32': '{}/.pyWebWatch/config.json'.format(homeDir)
}

def header():
    """
 _______  __   __  _     _  _______  _______  _     _  _______  _______  _______  __   __ 
|       ||  | |  || | _ | ||       ||  _    || | _ | ||   _   ||       ||       ||  | |  |
|    _  ||  |_|  || || || ||    ___|| |_|   || || || ||  |_|  ||_     _||       ||  |_|  |
|   |_| ||       ||       ||   |___ |       ||       ||       |  |   |  |       ||       |
|    ___||_     _||       ||    ___||  _   | |       ||       |  |   |  |      _||       |
|   |      |   |  |   _   ||   |___ | |_|   ||   _   ||   _   |  |   |  |     |_ |   _   |
|___|      |___|  |__| |__||_______||_______||__| |__||__| |__|  |___|  |_______||__| |__|
    """

def clearscreen():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # Linux or MacOS
        os.system('clear')
    elif platform == "win32":
        # Windows
        os.system('cls')

class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endcolor = '\033[0m'
    whitebold = '\033[1m'
    underline = '\033[4m'
    cyan = '\u001b[36m'
    cyanbold = '\u001b[36;1m'
    redbold = '\u001b[31;1m'
    yellowbold = '\u001b[33;1m'
    greenbold = '\u001b[32;1m'
    bluebold = '\u001b[34;1m'
    magentabold = '\u001b[35;1m'
    purplebold = '\u001b[35;1m'
    whitebolder = '\u001b[37;1m'
    reset = '\u001b[0m'

def menuItems():
    print(bcolors.)

def menu():
    try:
        choice = ''
        while choice not in ['e', 'E', 'd', 'D', '1', '2', 'q', 'Q']:
            clearscreen()
            header()
            menuiitems()
            choice = input('> ')
            if choice == 'e' or choice == 'E':
                encryptfile()
            elif choice == 'd' or 'D':
                decryptfile()
            elif choice == 'q' or choice == 'Q':
                exit(0)
    except KeyboardInterrupt:
        print("You want to leave so early?\nI thought we were just getting started!")

def main():
    menu()
