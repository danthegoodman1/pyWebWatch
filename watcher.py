import requests
from lxml import html
from os.path import expanduser
import sys
import json
from datetime import datetime

homeDir = expanduser("~")

configLocation = {
    'darwin': '{}/.pyWebWatch'.format(homeDir),
    'linux': '{}/.pyWebWatch'.format(homeDir),
    'linux2': '{}/.pyWebWatch'.format(homeDir),
    'win32': '{}/.pyWebWatch'.format(homeDir)
}

configFile = configLocation[sys.platform] + '/config.json'

def saveConfig(newConfig):
    saveFile = open(configFile, 'w')
    json.dump(newConfig, saveFile)
    saveFile.close()

def getConfig():
    with open(configFile) as jsonData:
        return json.load(jsonData)

def makePageObject(url):
    return {
        'url': url,
        'changes': 0,
        'lastChange': datetime.now()
    }

def getPage(pageURL):
    return requests.get(pageURL).text

def getPageTree(pageURL):
    page = requests.get(pageURL)
    tree = html.fromstring(page.content)
    return tree

def addPage():
    print('Alright, let\'s add a new page!')
    newPage = input('> ')
    oldData = getConfig()
    oldData['monitoredPages']

# Development printing

# print(checkPage('https://motherfuckingwebsite.com').xpath('//h1/text()')[0])
# print(getPage('https://motherfuckingwebsite.com/'))
