import requests
from bs4 import BeautifulSoup

page = requests.get("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2013")
page
print(page.status_code)

number_class = "montantpetit G"
strate_class = "montantpetit"

soup = BeautifulSoup(page.content, 'html.parser')

soup.find_all(class_= number_class)

price_text = soup.find_all(class_= number_class)
data = price_text[2]
print(data.prettify())

print(data.text.strip())