#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html
from os.path import expanduser
import sys
import json
from datetime import datetime
import watcher
import difflib

homeDir = expanduser("~")

configLocation = {
    'darwin': '{}/.pyWebWatch'.format(homeDir),
    'linux': '{}/.pyWebWatch'.format(homeDir),
    'linux2': '{}/.pyWebWatch'.format(homeDir),
    'win32': '{}/.pyWebWatch'.format(homeDir)
}

configFile = configLocation[sys.platform] + '/config.json'

key = open('iftttkey', 'r')
keydata = key.read().rstrip()

link = 'https://maker.ifttt.com/trigger/pywebwatch/with/key/{}'.format(keydata)

data = watcher.getConfig()

def emailAlert(url, diffData):
    body: {
        'value1': diffData
    }
    requests.post(link, body)

for idx, val in enumerate(data['monitoredPages']):
    oldPage = val['oldPage']
    newPage = watcher.getPage(val['url'])
    if oldPage != newPage:
        s1 = set(oldPage)
        s2 = set(newPage)
        diff = s2 - s1
        emailAlert(val['url'], diff)
