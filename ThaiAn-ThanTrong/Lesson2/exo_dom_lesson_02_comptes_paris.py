import requests
from bs4 import BeautifulSoup
import pandas as pd

### Count results for Paris from 2009 to 2013

years = ['2010', '2011', '2012', '2013']


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

    A = [int(val.text.strip().replace(' ', '')) for val in all_val[0:3]]
    B = [int(val.text.strip().replace(' ', '')) for val in all_val[3:6]]
    C = [int(val.text.strip().replace(' ', '')) for val in all_val[9:12]]
    D = [int(val.text.strip().replace(' ', '')) for val in all_val[12:15]]

    df_year = pd.DataFrame(A)
    df_year.index = ["En milliers d'euros", "Euros par habitant", "Moyenne de la strate"]
    df_year.columns = ['A']

    df_year['B'] = B
    df_year['C'] = C
    df_year['D'] = D

    return df_year


def get_soup_all():
    columns = ['A', 'B', 'C', 'D']

    df_ = pd.DataFrame(index=years, columns=columns)

    for year in years:
        df_tmp = get_soup_year(year)
        print(df_tmp)

    return df_

print(get_soup_all())
