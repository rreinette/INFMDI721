#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:56:34 2017

@author: maha
"""
import requests
from bs4 import BeautifulSoup




url = ''
res= requests.get(url)

soup= BeautifulSoup(res.text,'html.parser')

((class, ))
print int(soup.find_all(class_=classname)[0].text
          
          )

