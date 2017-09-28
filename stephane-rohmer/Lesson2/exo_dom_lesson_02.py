#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:19:00 2017

@author: charlesrohmer
"""

import requests
from bs4 import BeautifulSoup




def getSoupFromURL(url, method='get', data={}):
#   
#   Appel de la fonction vu en cours pour construire la soupe à partir d'url
#   
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


def insertInList(my_soup):  
#   
#    Sort un tableau des 4 premieres column de la source, trié par les tr puis td
#    Ne traite que des strings, on peut améliorer en transformant les donnée num
#    en float
#
       
    tab=[]
    for rows in soup.find_all('tr',{"class":"bleu"}):
        #initiaisation des lignes par le tag TR
        lines = []
        cols = rows.find_all('td')
        
        for i,td in enumerate(cols):
            # on ne récupère que les 4 premières colunnes. 
            # si l'index est inférieur à 4, alors on insert, sinon on fait rien
            if i < 4:
                data = td.string
                lines.append(data)
                
        # on insert le résultat de chaque ligne dans le tableau final        
        tab.insert(-1,lines)
 
    return tab

result = []

# l'url est fixe sauf pour l'année, donc à chaque année on relance les 2 fonctions
# on aggrège dnas la variable resultat
for exercice in range(2010,2016):
    resulta = []
    my_url = "http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=" + str(exercice)
    
    soup = getSoupFromURL(my_url)        
    resulta = insertInList(soup)
    result.append(resulta)

print (result)


