#exercice de web scrapping

from bs4 import BeautifulSoup
import requests
from urllib2 import urlopen

an_10 = urlopen('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2010').read()
an_11 = urlopen('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2011').read()
an_12 = urlopen('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2012').read()
an_13 = urlopen('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2013').read()
an_14 = urlopen('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2014').read()
an_15 = urlopen('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2015').read()
soup10 = BeautifulSoup(an_10, 'lxml')
for i in soup10.find_all('td', class_='montantpetit G')[1:3]:
    print i.string

soup11 = BeautifulSoup(an_11, 'lxml')
for i in soup11.find_all('td', class_='montantpetit G')[1:3]:
    print i.string

soup12 = BeautifulSoup(an_12, 'lxml')
for i in soup12.find_all('td', class_='montantpetit G')[1:3]:
    print i.string

soup13 = BeautifulSoup(an_13, 'lxml')
for i in soup13.find_all('td', class_='montantpetit G')[1:3]:
    print i.string

soup14 = BeautifulSoup(an_14, 'lxml')
for i in soup14.find_all('td', class_='montantpetit G')[1:3]:
    print i.string

soup15 = BeautifulSoup(an_15, 'lxml')
for i in soup15.find_all('td', class_='montantpetit G')[1:3]:
    print i.string
