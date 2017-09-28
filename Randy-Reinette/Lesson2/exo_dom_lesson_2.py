import requests
from bs4 import BeautifulSoup

base_url = "http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice="
class_to_find = "montantpetit G"
def getSoupFromURL(url):
 	res= requests.get(url)
	if res.status_code == 200:
		soup = BeautifulSoup(res.text,'html.parser')
		return soup
	else:
		return None

def getCountResult(url,className,position):
	soup = getSoupFromURL(url)
	if soup:
		resultArray = soup.findAll(class_=className)
		return resultArray[position].text.strip()
for year in range(2010,2015):
	print "====Result for year "+str(year)+"===="
	print"Result data column A: \n",getCountResult(base_url+str(year),class_to_find,1),"euros per inhabitant \n",getCountResult(base_url+str(year),class_to_find,2),"euros average for the layer"
	
	print"Result data column B: \n",getCountResult(base_url+str(year),class_to_find,4),"euros per inhabitant \n",getCountResult(base_url+str(year),class_to_find,5),"euros average for the layer"
	
	print"Result data column C: \n",getCountResult(base_url+str(year),class_to_find,7),"euros per inhabitant \n",getCountResult(base_url+str(year),class_to_find,8),"euros average for the layer"

	print"Result data column D: \n",getCountResult(base_url+str(year),class_to_find,10),"euros per inhabitant \n",getCountResult(base_url+str(year),class_to_find,11),"euros average for the layer"
	print"============================"
