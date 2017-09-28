#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:15:40 2017

@author: mehdiregina
"""

import requests
from bs4 import BeautifulSoup

def get_soup_from_url(annee):
    """Retourne BeautifulSoup object associé aux resultat des comptes de Paris de 
    l'année passée en paramètre"""
    try:
        url="http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice="+str(annee)
    except(ValueError):
        print("L'année voulue doit être passée en paramètre, par exemple 2012")
    page=requests.get(url)
    return BeautifulSoup(page.content,'html.parser')

def data_treatment(string):
    """prend en entré le get_text et retour l'int associé"""
    return int("".join(string.strip('\xa0').split()))

def get_data(annee):
    """Retourne les valeurs des données ABCD pour l'année voulue)"""
    soup=get_soup_from_url(annee)
    
    #1e méthode
    #découpe mes div
    #liste_div_bleu=soup.select(".bleu")
    #sélection 2e child de chaque div
    #liste_2e=[bloc.select("td:nth-of-type(2)") for bloc in liste_div_bleu]

    
    #2e méthode
    liste_div_nb=soup.select(".montantpetit.G")
    index_per_hab=[1,4,10,13]
    index_moy=[2,5,11,14]
    index_lettres=["A","B","C","D"]
    data_eur_per=[data_treatment(liste_div_nb[i].get_text()) for i in index_per_hab]
    data_moy=[data_treatment(liste_div_nb[i].get_text()) for i in index_moy]
    return index_lettres,data_eur_per,data_moy
    
    

index_lettres_12,data_eur_per_12,data_moy_12=get_data(2012)
index_lettres_13,data_eur_per_13,data_moy_13=get_data(2013)
index_lettres_14,data_eur_per_14,data_moy_14=get_data(2014)
index_lettres_15,data_eur_per_15,data_moy_15=get_data(2015)
