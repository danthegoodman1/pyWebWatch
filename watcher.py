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

def getPage(pageURL):
    return requests.get(pageURL).text

def getPageTree(pageURL):
    page = requests.get(pageURL)
    tree = html.fromstring(page.content)
    return tree

def makePageObject(url):
    return {
        'url': url,
        'changes': 0,
        'lastChange': str(datetime.now()),
        'oldPage': getPage(url),
        'newPage': ''
    }

def addPage():
    print('Alright, let\'s add a new page!\nWhat\'s the URL?')
    newPage = input('> ')
    newData = getConfig()
    newData['monitoredPages'].append(makePageObject(newPage))
    saveConfig(newData)

def removePage():
    print('Alright let\'s remove a page, what is the URL you want to remove?')
    removeURL = input('> ')
    data = getConfig()
    for idx, val in enumerate(data['monitoredPages']):
        if removeURL in val['url']:
            del data['monitoredPages'][idx]
            print('Removed ' + removeURL)
    saveConfig(data)
            

# Development printing

# print(checkPage('https://motherfuckingwebsite.com').xpath('//h1/text()')[0])
# print(getPage('https://motherfuckingwebsite.com/'))
