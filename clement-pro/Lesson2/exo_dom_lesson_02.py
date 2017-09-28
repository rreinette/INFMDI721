import urllib.request
from bs4 import BeautifulSoup


years = range(2000,2016)
labels = ["TOTAL DES PRODUITS DE FONCTIONNEMENT = A", "TOTAL DES CHARGES DE FONCTIONNEMENT = B", "TOTAL DES RESSOURCES D'INVESTISSEMENT = C", "TOTAL DES EMPLOIS D'INVESTISSEMENT = D"]
value_per_capita_per_year = []


for year in years:

    icom = "101" if year < 2010 else "056"
    url = "http://alize2.finances.gouv.fr/communes/eneuro/tableau.php?icom=" + icom \
          + "&dep=075&type=BPS&param=0&exercice=" + str(year)

    with urllib.request.urlopen(url) as my_html:
        my_soup = BeautifulSoup(my_html, 'html.parser')

    value_per_capita = []

    for label in labels:
        tag_of_interest = my_soup.find("td", string=label).parent.select('td:nth-of-type(3)')[0]
        value_per_capita.append(int("".join(tag_of_interest.text.split())))

    value_per_capita_per_year.append(value_per_capita)

print(value_per_capita_per_year)
