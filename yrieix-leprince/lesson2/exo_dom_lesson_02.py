import requests
from bs4 import BeautifulSoup

"""
Scroller le résultat des comptes de la ville de Paris pour les exercices 2009 à 2013.
Récupérer les données A,B,C et D sur les colonnes Euros par habitant et par strate.
"""

root = "http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice="
urls = [root + str(year) for year in range(2010, 2016)]


for url in urls:

    print(url[-4:]+":")

    htmlContent = requests.get(url).text
    soup = BeautifulSoup(htmlContent, 'html.parser')

    nthIndexes = {'A':{'euroHab':16, 'avStrat':17}, 'B':{'euroHab':39, 'avStrat':40},
               'C':{'euroHab':84, 'avStrat':85}, 'D':{'euroHab':113, 'avStrat':114}}

    for superKey in nthIndexes:
        for key in nthIndexes[superKey]:
            print("\t", superKey, key, int(soup.select_one("tr td:nth-of-type(%s)"
                    % nthIndexes[superKey][key]).text.strip().replace(" ", "")))
        print()

    print("------\n")
