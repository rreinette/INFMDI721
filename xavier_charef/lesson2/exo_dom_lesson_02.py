import requests
from bs4 import BeautifulSoup
import re

url = "http://alize2.finances.gouv.fr/communes/eneuro/detail.php"
class_tr_data="tr.bleu"
class_result = "montantpetit G"


# methode extrayant les valeurs le code source de la page html associée à l'url mise en parametre
def getSoupFromUrlInPost(url, url_data):

    result_result = requests.post(url, url_data)
    if result_result.status_code == 200:
        soup_result = BeautifulSoup(result_result.text, 'html.parser')
        return soup_result
    else:
        return None


#methode renvoyant les valeurs des titres des données A,B,C et D
def getTitreDataABCD(soup):
    titre_data=[]

    for css_selector in ['td:nth-of-type(%s)' % i for i in [18, 41, 86, 115]]:
        data = soup.select(css_selector)[0].text.strip()[:-4]
        titre_data.append(data)
    return titre_data


#methode renvoyant les valeurs de la colonne Euros par strates pour les données A,B,C et D
def getEurosParHabitantDataABCD(soup):
    soup_result = soup.find_all("td", class_=class_result)

    montant_data_list = [int(soup_result[i].text.strip().replace(" ", "")) for i in [1, 5, 11, 14]]

    #montant_data_dico=[{"TOTAL DES PRODUITS DE FONCTIONNEMENT":,"TOTAL DES CHARGES DE FONCTIONNEMENT":, "TOTAL DES RESSOURCES D'INVESTISSEMENT":, "TOTAL DES EMPLOIS D'INVESTISSEMENT":}]
    return montant_data_list


#methode renvoyant les valeurs de la colonne Euros par strates pour les données A,B,C et D
def getEurosParStrateDataABCD(soup):
    soup_result = soup.find_all("td", class_=class_result)
    # regex = r'<td class=\"montantpetit G\">(.*)<\/td>'

    montant_data_list = [int(soup_result[i].text.strip().replace(" ", "")) for i in [1, 5, 11, 14]]
    return montant_data_list


# Execution des methodes pour les années de 2010 à 2015
print("Lancement du programme d'extraction des données du site web de la mairie de Paris")
for date in range(2010, 2016):
    url_data = {'ICOM': '056','DEP':'075','TYPE':'BPS','PARAM':0,'dep':'','reg':'','nomdep':'','moysst':'','exercice':'','param':'','type':'','siren':'','comm':0,
'EXERCICE':date}
    soup = getSoupFromUrlInPost(url, url_data)
    if soup == None:
        print("Le programme n'a pas pu se connecter au site web de la mairie de Paris")
    else:
        print()
        print("Detail des budgets par Habitant et par Strate de l'année %s:" % date)
        print()
        for i in range(4):
            print(getTitreDataABCD(soup)[i]+": ", " pour les montants par habitant: " + "%s" % getEurosParHabitantDataABCD(soup)[i] + ", ", " pour les montants par strate: " + "%s" % getEurosParStrateDataABCD(soup)[i])
        #print("Detail des budgets par Strate de l'année %s" % date)
        #print(getEurosParStrateDataABCD(url, url_data))


