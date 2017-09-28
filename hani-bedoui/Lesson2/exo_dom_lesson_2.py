# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
 

"""


import requests
from bs4 import BeautifulSoup

url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice='
number_class='montantpetit G'


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

def getNumber(url, classname,num):
  soup = getSoupFromURL(url)
  if soup:

    all_bold_numbers = soup.find_all(class_=classname)
    return all_bold_numbers[num].text.strip()

for i in range (2010,2016):
    
    print("Anneé " + str(i) + "\n\n")
    
    print('A : '+"\n"+ getNumber(url+str(i),number_class, 1), ' Euros par habitant' + "\n" 
          'Moyenne de la strate: ',getNumber(url+str(i),number_class, 2) + "\n")
    print('B : '+"\n"+ getNumber(url+str(i),number_class, 4), ' Euros par habitant' + "\n" 
          'Moyenne de la strate: ',getNumber(url+str(i),number_class, 5) + "\n")
    print('C : '+"\n"+ getNumber(url+str(i),number_class, 10), ' Euros par habitant' + "\n" 
          'Moyenne de la strate: ',getNumber(url+str(i),number_class, 11) + "\n")
    print('D : '+"\n"+ getNumber(url+str(i),number_class, 10), ' Euros par habitant' + "\n" 
          'Moyenne de la strate: ',getNumber(url+str(i),number_class, 11) + "\n")
   
    
    
    
  
    
