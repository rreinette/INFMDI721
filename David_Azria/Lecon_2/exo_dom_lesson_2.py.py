#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:17:23 2017
@author: david
"""
import requests
from bs4 import BeautifulSoup
import urllib.request

année=[2010,2011,2012,2013,2014,2015]


print ("Je n'ai pas capté l'histoire de la colonne par strate")
for an in année:
        
    url=urllib.request.urlopen("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice={0}".format(an))

    soup = url.read()
    soup = BeautifulSoup(soup,"lxml")
    titre=soup.find_all(align="right")
    titre=titre[1].text
    
    u=soup.find_all('td',"montantpetit G")
    print ("Resultats de l'année ",titre)
    print("A",u[1].text,"€  moyenne par habitant")
    print ("B",u[4].text,"€  moyenne par habitant")
    print ("C",u[10].text,"€  moyenne par habitant")
    print ("D",u[13].text,"€  moyenne par habitant")
    
    print(" Paris étant la seule occurence dans sa strate, la moyenne par strate est identique")
    print("A",u[1+1].text,"€  moyenne par strate")
    print ("B",u[4+1].text,"€  moyenne par strate")
    print ("C",u[10+1].text,"€  moyenne par strate")
    print ("D",u[13+1].text,"€  moyenne par strate")
    print ("CQFD")


#v=range(50)
#num=1
#for num in v :
#    print(soup.select("tr.bleu:nth-of-type('num')"))
    