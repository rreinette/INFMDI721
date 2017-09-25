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

    td_tag_search = my_soup.find_all("td", class_="libellepetit")

    all_td_labels = [td.text.strip() for td in td_tag_search]

    value_per_capita = []

    for label in labels:
        # search for label index in file
        value_per_capita.append(int("".join(td_tag_search[all_td_labels.index(label)].find_next_sibling().find_next_sibling().text.split())))
    value_per_capita_per_year.append(value_per_capita)

print(value_per_capita_per_year)
