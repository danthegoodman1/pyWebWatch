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

data = watcher.getConfig()

def emailAlert(url, diffData):
    pass

for idx, val in enumerate(data['monitoredPages']):
    oldPage = val['oldPage']
    newPage = watcher.getPage(val['url'])
    if oldPage != newPage:
        diff = difflib.ndiff(oldPage, newPage)
        emailAlert(val['url'], diff)
