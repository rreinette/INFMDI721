import requests
from bs4 import BeautifulSoup




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

def getNumberOfSharesForPage(url, classname, nb):
  soup = getSoupFromURL(url)
  if soup:
    share_content = soup.find_all(class_=classname)[nb].text.strip()
    return share_content
  else:
    return 0

for i in range (2010,2016):
    url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice='+str(i)
    share_class_pp = "montantpetit G"
    
    print("Pour l'annee ", i, ":")
    print()
    print("Pour A:")
    print("Euros par habitant: ",getNumberOfSharesForPage(url, share_class_pp, 1))
    print("Moyenne de la strate: ",getNumberOfSharesForPage(url, share_class_pp, 2))
    print()

    print("Pour B:")
    print("Euros par habitant: ",getNumberOfSharesForPage(url, share_class_pp, 4))
    print("Moyenne de la strate: ",getNumberOfSharesForPage(url, share_class_pp, 5))
    print()

    print("Pour C:")
    print("Euros par habitant: ",getNumberOfSharesForPage(url, share_class_pp, 10))
    print("Moyenne de la strate: ",getNumberOfSharesForPage(url, share_class_pp, 11))
    print()

    print("Pour D:")
    print("Euros par habitant: ",getNumberOfSharesForPage(url, share_class_pp, 13))
    print("Moyenne de la strate: ",getNumberOfSharesForPage(url, share_class_pp, 14))
    print("----------------------------------")
    print("----------------------------------")
    print()