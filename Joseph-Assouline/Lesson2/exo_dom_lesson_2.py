#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:59:40 2017

@author: joseph
"""

import urllib
from bs4 import BeautifulSoup
import requests
import re
import numpy as np

#def GetElement(text, )
#

def getData(year):
    year.sort()
    a=np.arange((year[-1]-year[0]+1)*8).reshape(year[-1]-year[0]+1,8)
    i=0
    url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice='
    urllist=[]
    urllist= list(map(lambda y : url +str(y), year))
    for url in urllist:
        a[i]=GetElement2(url)
        i+=1
    print('la matrice résultat est', a)
    return a    
    
def GetElement(url):
    montant=np.array([0,0,0,0])
    res= requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    mydivs=soup.find_all( class_ = "montantpetit G")
    regex =r"(<td class=\"montantpetit G\">)(.*)\s</td>+"
    montant[0] = int(re.search(regex,str(mydivs[2]))[2].replace(' ',''))
    montant[1] = int(re.search(regex,str(mydivs[4]))[2].replace(' ',''))
    montant[2] = int(re.search(regex,str(mydivs[10]))[2].replace(' ',''))
    montant[3] = int(re.search(regex,str(mydivs[14]))[2].replace(' ',''))
#    print('for'+url +'we got the following: \n', montant)
    return montant

def GetElement2(url):
    montant=np.array([0,0,0,0,0,0,0,0])
    regex =r"(<td class=\"montantpetit G\">)(.*)\s</td>+"
    res= requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    ResulTableA= soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")
    ResulTableB= soup.find("td", text="TOTAL DES CHARGES DE FONCTIONNEMENT = B").parent.find_all(class_ = "montantpetit G")
    ResulTableC= soup.find("td", text="TOTAL DES RESSOURCES D'INVESTISSEMENT = C").parent.find_all(class_ = "montantpetit G")
    ResulTableD= soup.find("td", text="TOTAL DES EMPLOIS D'INVESTISSEMENT = D").parent.find_all(class_ = "montantpetit G")
#    print(ResulTableB[2].text,ResulTableC[2].text,ResulTableD[2].text)
    for i in range(0,2):
        montant[i]=int(ResulTableA[i+1].text.replace(' ',''))
        montant[i+2]=int(ResulTableB[i+1].text.replace(' ',''))
        montant[i+4]=int(ResulTableC[i+1].text.replace(' ',''))
        montant[i+6]=int(ResulTableD[i+1].text.replace(' ',''))
    print(montant)
    return montant
#    montant[0] = int (soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    montant[0] = int (soup.find("td", text="TOTAL DES CHARGES DE FONCTIONNEMENT = B").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    montant[0] = int (soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    montant[0] = int (soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    montant[0] = int (soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    montant[0] = int (soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    montant[0] = int (soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    montant[0] = int (soup.find("td", text="TOTAL DES PRODUITS DE FONCTIONNEMENT = A").parent.find_all(class_ = "montantpetit G")[1].text.replace(' ',''))
#    print(Inter)    

    
    
    
def test()   :
    
    Year=[2010,2011,2012,2013,2014,2015]
    getData(Year)


GetElement2("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2013")
test()
#test()
    

#GetElement("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2015")   