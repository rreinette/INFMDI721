import requests
from bs4 import BeautifulSoup

url='http://www.purepeople.com/article/laeticia-et-johnny-hallyday-leur-fille-jade-franchit-un-cap-avec-le-sourire_a252004/1'
share_class_pp="c-sharebox__stats-number"

def getSoupFromURL(url, method='get',data={}):
  if method=='get':
    res=requests.get(url)
  elif method=='post':
    res=request
  else:
    return None






def getNumberOfSharesForPage(url,classname):
  soup=getSoupFromURL(
  if soup:
    return int(
  else:
    0



