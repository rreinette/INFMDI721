
# coding: utf-8


#Scraping Paris city budget facts
## From year 2010 to 2015
### source : http://alize2.finances.gouv.fr




# Importing library
import csv
from urllib import urlopen
from bs4 import BeautifulSoup
import requests


## Scraping all the elements of the first table and store it in a CSV for further usage (recommended in case the data
## would not be available anymore)

def PageParisBudgetToCsv(firstyear,lastyear):
    """
    Params
    firstyear : first budget year to be collected
    lastyear : last budget year to be collected
    """
    for year in range(firstyear,lastyear+1):
        csvFile = open("paris%d.csv"%year, 'wt')
        writer = csv.writer(csvFile)

        baseurl = "http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice="
        url = baseurl+str(year)
        html = requests.get(url).text
        bsObj = BeautifulSoup(html)
        table = bsObj.findAll("table")[2]
        rows = table.findAll("tr")

        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text().encode('utf8'))
            writer.writerow(csvRow)
        csvFile.close()



PageParisBudgetToCsv(2010,2015)


#Choosing a year to display budget values

def DisplayMainValues(year):
    yearAvailable = range(2010,2016)
    if year in yearAvailable:

        with open("paris%d.csv"%year) as f:
            reader = csv.reader(f,delimiter=',')
            lookup = ['TOTAL DES PRODUITS DE FONCTIONNEMENT = A','TOTAL DES CHARGES DE FONCTIONNEMENT = B',
                      'TOTAL DES RESSOURCES D\'INVESTISSEMENT = C', 'TOTAL DES EMPLOIS D\'INVESTISSEMENT = D']
            #reader.filter(lambda x : x in lookup )
            #for i in lookup:
            for row in reader:
                #any(i in a for i in b)
                #print row
                if bool(set(row) & set(lookup)):
                #any(elem in lookup for i in row  ):
                    #print row
                    print row[3][:-4].capitalize()+" par habitant en "+str(year)+" : "+row[1]
                    print row[3][:-4].capitalize()+" par strate en "+str(year)+" : "+row[2]
    else:
        print "Cette annee n'est pas disponible dans l'historique"


#Testing the display
DisplayMainValues(2010)

