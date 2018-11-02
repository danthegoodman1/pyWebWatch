#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Made with ❤ By Dan Goodman
"""

# Imports
import sys
import watcher
from os.path import expanduser
import os
from time import sleep
import json

class colors:
    purple = '\033[0;95m'
    blue = '\033[0;94m'
    green = '\033[0;32m'
    yellow = '\033[0;93m'
    red = '\033[0;91m'
    whitebold = '\033[0;1m'
    underline = '\033[0;4m'
    cyan = '\033[0;36m'
    cyanbold = '\033[1;36m'
    redbold = '\033[1;31m'
    yellowbold = '\033[1;33m'
    greenbold = '\033[1;32m'
    bluebold = '\033[1;34m'
    purplebold = '\033[1;95m'
    magentabold = '\033[1;35m'
    whitebolder = '\033[1;37m'
    endcolor = '\033[0m'
    reset = '\033[0m'
    lightgreen = '\033[0;92m'
    fadedgreen = '\033[2;92m'
    fadedyellow = '\033[2;93m'

homeDir = expanduser("~")

configLocation = {
    'darwin': '{}/.pyWebWatch'.format(homeDir),
    'linux': '{}/.pyWebWatch'.format(homeDir),
    'linux2': '{}/.pyWebWatch'.format(homeDir),
    'win32': '{}/.pyWebWatch'.format(homeDir)
}

configFile = configLocation[sys.platform] + '/config.json'

if os.path.isfile(configFile):
    with open(configFile) as jsonData:
        loadedConfig = json.load(jsonData)
elif os.path.isdir(configLocation[sys.platform]):
    createdFile = open(configFile, 'w')
    createdFile.write('{}')
    createdFile.close()
    print(colors.blue + 'Creating config file...')
else:
    os.mkdir(configLocation[sys.platform])
    createdFile = open(configFile, 'w')
    createdFile.write('{}')
    createdFile.close()
    print(colors.blue + 'Creating config folder and file...')



def header():
    print(colors.purple + """
 _______  __   __  _     _  _______  _______  _     _  _______  _______  _______  __   __ 
|       ||  | |  || | _ | ||       ||  _    || | _ | ||   _   ||       ||       ||  | |  |
|    _  ||  |_|  || || || ||    ___|| |_|   || || || ||  |_|  ||_     _||       ||  |_|  |
|   |_| ||       ||       ||   |___ |       ||       ||       |  |   |  |       ||       |
|    ___||_     _||       ||    ___||  _   | |       ||       |  |   |  |      _||       |
|   |      |   |  |   _   ||   |___ | |_|   ||   _   ||   _   |  |   |  |     |_ |   _   |
|___|      |___|  |__| |__||_______||_______||__| |__||__| |__|  |___|  |_______||__| |__|
    """ + colors.yellow + " Made with" + colors.red + " ❤ " + colors.yellow + "By Dan Goodman\n " + colors.endcolor)

def clearscreen():
    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
        # Linux or MacOS
        os.system('clear')
    elif sys.platform == "win32":
        # Windows
        os.system('cls')

def menuInfo():
    print(colors.fadedyellow + 'Config loaded from: ' + colors.fadedgreen + configFile + colors.reset)
    print(colors.yellowbold + 'Currently monitoring: ' + colors.reset + 'https://google.com')
    print(colors.cyanbold + 'Last change: ' + colors.reset + colors.reset + 'never')
    print(colors.bluebold + 'Change count: ' + colors.reset + str(3))

def menu():
    try:
        choice = ''
        while choice not in ['c', 'r', 'q']:
            clearscreen()
            header()
            menuInfo()
            print(colors.purplebold + 'Welcome to the main menu!' + colors.reset + colors.green + '\n  Would you like to:' + colors.reset)
            print(colors.blue + '       Change a currently monitored page [c]' + colors.reset)
            print(colors.blue + '       Remove a currently monitored page [r]' + colors.reset)
            print(colors.blue + '       Quit [q]' + colors.reset)
            print(colors.purple)
            choice = input(colors.reset + colors.red + '> ' + colors.reset).lower()
            if choice == 'c':
                pass
            elif choice == 'r':
                pass
            elif choice == 'q':
                exit(colors.red + 'See ya!' + colors.reset)
    except KeyboardInterrupt:
        print(colors.redbold + "\nYou want to leave so early?\nI thought we were just getting started!" + colors.reset)

def main():
    menu()

main()
