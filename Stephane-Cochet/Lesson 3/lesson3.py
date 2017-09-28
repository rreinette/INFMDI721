#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 07:21:55 2017

@author: cochet
"""

#import urllib2
import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2013'

def getSoupFromURL(url, method='get', data={}):

  if method == 'get':
    res = requests.get(url)
  elif method == 'post':
    res = requests.post(url, data=data)
  else:
    return None

  if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
  else:
    return None



soup = getSoupFromURL(url)

class_result = "montantpetit G"




