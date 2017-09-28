import requests
from bs4 import BeautifulSoup


url = 'http://www.purepeople.com/article/caroline-de-maigret-ce-jour-ou-yarol-poupaud-a-quitte-sa-copine-pour-elle_a251827/1'
share_class_pp = "c-sharebox__stats-number"

#méthode partant de l'url passant par un response object puis renvoyant un beautifulsoup object
def getSoupFromURL(url, method='get', data={}):

  if method == 'get':
    res = requests.get(url) #je télécharge la page : Requests data from a specified resource
  elif method == 'post': #Submits data to be processed to a specified resource
    res = requests.post(url, data=data)
  else:
    return None

  if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser') #je cree mon beautifulsoup obj
    return soup
  else:
    return None

#je pars de mon beautiful soup object et je renvois le nombre de partages
def getNumberOfSharesForPage(url, classname):
  soup = getSoupFromURL(url)
  if soup:
      # le but ici est de mettre la classe du tag contenant le nombre de partages
      #et de récupérer le nb de partage (1er elmt de la liste cree)
    share_content = soup.find_all(class_=classname)[0].text.strip() #pq pas .get_text
    if 'K' in share_content:
      #si K petite opération pour convertion en milliers
      parts = share_content[:-1].split(',')
      return int(parts[0])*1000 + int(parts[1])*100
    else:
      return int(share_content)
  else:
    0

def getListOfArticlesForPeople(people):
  #url_search = "http://www.purepeople.com/rechercher/"
  #params = {"q": people}
  #results_search  = getSoupFromURL(url_search, 'post', params)

  url_search = "http://www.purepeople.com/rechercher/q/" + people + "/cat/article/np/"
  class_result = "c-article-flux__title"
  results_search = []
  for i in range(1,2):
    #je renvois mon soup object associé à la première, puis dans un 2nd temps à la deuxième page
    soup_results_search  = getSoupFromURL(url_search+str(i))
    #je stocke dans une liste le lien derrière href associée à la balise a pour chaque page
    results_search += [a['href'] for a in soup_results_search.find_all("a", class_=class_result)]
  return results_search


#all_pages_people_1 = getListOfArticlesForPeople('johnny')
#je retourne la liste des liens de tous les articles associés au mot angelina
all_pages_people_2 = getListOfArticlesForPeople('angelina')

#shares_people_1 = []
shares_people_2 = []
#pour chaque lien d'article, je récupère le nombre de partage que je stocke dans la liste share people
for page in all_pages_people_2:
  print '-----'
  print page
  share = getNumberOfSharesForPage("http://www.purepeople.com" + page, share_class_pp)
  print share
  shares_people_2.append(share)
