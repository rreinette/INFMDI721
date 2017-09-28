import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice='
bn_class = 'montantpetit G'
years = [2010,2011,2012,2013,2014,2015]
position_eur_hab = [2,5,11,14]
position_moy_strate = [3,6,12,15]

labels = ['Euros par habitant A','Euros par habitant B','Euros par habitant C',
         'Euros par habitant D','Moyenne de la strate A','Moyenne de la strate B',
         'Moyenne de la strate C','Moyenne de la strate D']
results_table = pd.DataFrame({'2010': [0]*8, '2011': [0]*8, '2012': [0]*8, '2013': [0]*8,
                               '2014': [0]*8, '2015': [0]*8,})
results_table.index = labels

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

def getBoldNumbers(url, classname, number):
  soup = getSoupFromURL(url)
  if soup:
    bold_number = soup.find_all(class_=classname)[number].text.strip()
    return bold_number
  else:
    return 0

for i in years:
  for x in range(0,4):
    results_table[str(i)][x] = getBoldNumbers(url + str(i), bn_class, position_eur_hab[x]).replace(" ", "")      
  for y in range(0,4):
    results_table[str(i)][y+4] = getBoldNumbers(url + str(i), bn_class, position_moy_strate[y]).replace(" ", "")

results_table