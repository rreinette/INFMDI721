import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Count results for Paris from 2010 to 2015

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


def get_soup_year(year):
    url_search = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=' + year
    class_results = 'montantpetit G'

    soup = getSoupFromURL(url_search)

    all_val = soup.find_all(class_=class_results)

    A = [int(val.text.strip().replace(' ', '')) for val in all_val[1:3]]
    B = [int(val.text.strip().replace(' ', '')) for val in all_val[4:6]]
    C = [int(val.text.strip().replace(' ', '')) for val in all_val[10:12]]
    D = [int(val.text.strip().replace(' ', '')) for val in all_val[13:15]]

    return A, B, C, D


def get_soup_year_css(year):
    url_search = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=' + year
    class_results = "libellepetit G"

    soup = getSoupFromURL(url_search)

    res = soup.find_all("td", class_=class_results)

    euros_par_hab = [int(r.parent.select_one("td:nth-of-type(2)").text.replace('\xa0', '').replace(' ', '')) for r in
                     res if
                     re.search('= [ABCD]\Z', r.text)]
    moyenne_par_strate = [int(r.parent.select_one("td:nth-of-type(3)").text.replace('\xa0', '').replace(' ', '')) for r
                          in res if
                          re.search('= [ABCD]\Z', r.text)]

    dict_euros = dict()
    dict_euros[year] = euros_par_hab

    dict_strate = dict()
    dict_strate[year] = moyenne_par_strate

    return dict_euros, dict_strate


# Reorganise the extracted data
def get_soup_all(years):
    columns = ['A', 'B', 'C', 'D']

    df_euros_hab = pd.DataFrame(index=years, columns=columns)
    df_euros_hab.name = 'Euros par habitant'

    df_moyenne_strat = pd.DataFrame(index=years, columns=columns)
    df_moyenne_strat.name = 'Moyenne de la strate'

    for year in years:
        A, B, C, D = get_soup_year(year)
        df_euros_hab.loc[year, 'A':'D'] = A[0], B[0], C[0], D[0]
        df_moyenne_strat.loc[year, 'A':'D'] = A[1], B[1], C[1], D[1]

    return df_euros_hab, df_moyenne_strat


def get_soup_all_css(years):
    columns = ['A', 'B', 'C', 'D']

    df_euros_hab = pd.DataFrame(index=years, columns=columns)
    df_euros_hab.name = 'Euros par habitant'

    df_moyenne_strat = pd.DataFrame(index=years, columns=columns)
    df_moyenne_strat.name = 'Moyenne de la strate'

    for year in years:
        dict_euros, dict_strate = get_soup_year_css(year)
        df_euros_hab.loc[year, 'A':'D'] = dict_euros[year]
        df_moyenne_strat.loc[year, 'A':'D'] = dict_strate[year]

    return df_euros_hab, df_moyenne_strat


if __name__ == "__main__":
    years = ['2010', '2011', '2012', '2013', '2014', '2015']
    # print('-------- FIRST ATTEMPT --------')
    # df_euros_hab, df_moyenne_strat = get_soup_all(years)
    # print('Euros par habitant')
    # print(df_euros_hab)
    # print()
    #
    # print('Moyenne par strate')
    # print(df_moyenne_strat)
    # print('------------------------------')
    print('------ SECOND ATTEMPT --------')
    df_euros_hab_css, df_moyenne_strat_css = get_soup_all_css(years)
    print('Euros par habitant')
    print(df_euros_hab_css)
    print()

    print('Moyenne par strate')
    print(df_moyenne_strat_css)
    print('------------------------------')
