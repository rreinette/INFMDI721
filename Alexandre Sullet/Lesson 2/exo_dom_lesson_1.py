import requests
import re
import unittest

def getComptesComunnes(column,year):

	# Teste si l'année existe
	url = getUrlForYear(year)

	# Requete l'URL
	if url:	
		htmlText = requests.get(url).text
	else:
		return "Colonne ou Année non disponible"
	# Teste si la colonne existe et execute la premiere partie du regex
	regex1 = getRegexForColumn(column)

	# Effectue la deuxième regex
	regex2 = r"(<td class=\"montantpetit G\">)(.*?)(?=&nbsp;</td>)"

	if regex1 and regex2:
		matches = getMatchesForRexex(regex1, regex2, htmlText)
		return "Colonne " + column + ", Année " + year + " : " + getCountFromMatches(matches)
	else:
		return "Colonne ou Année non disponible"


def getRegexForColumn(column):
	if column == "A":
		return r"(<td class=\"montantpetit G\">)(.*?)(?=TOTAL DES PRODUITS DE FONCTIONNEMENT = A<\/td>)"
	elif column == "B":
		return r"(<td class=\"montantpetit G\">)(.*?)(?=TOTAL DES CHARGES DE FONCTIONNEMENT = B<\/td>)"
	elif column == "C":
		return r"(<td class=\"montantpetit G\">)(.*?)(?=TOTAL DES RESSOURCES D'INVESTISSEMENT = C<\/td>)"
	elif column == "D":
		return r"(<td class=\"montantpetit G\">)(.*?)(?=TOTAL DES EMPLOIS D'INVESTISSEMENT = D<\/td>)"
	else:
		return False


def getUrlForYear(year):
	if 2010 <= int(year) <= 2015: 
		return "http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=" + year
	else:
		return False

def getMatchesForRexex(regex1, regex2, htmlText):
	# Prend le Full Match [0] et garde les 180 derniers caractères
	matches1 = re.search(regex1, htmlText, re.DOTALL)[0][-180:]

	matches2 = re.finditer(regex2,matches1, re.DOTALL)

	return matches2

def getCountFromMatches(matches):
	# Récupère la bonne donnée de compte
	for matchNum, match in enumerate(matches):
		if matchNum == 2:
			return  match[2]

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (prefix + ' got: ' +  repr(got) +  ' expected: ' + repr(expected))


def main():

	continuer = True

	while continuer :
		print("Rentrez une année")
		year = input()
		print("Rentrez une colonne")
		column = input()
		print(getComptesComunnes(column,year))
		print("Voulez vous continuer ? (y/n)")
		if input() == "n":
			continuer = False



	# Bon tests

	print("Tests")
	# print(getComptesComunnes("A","2014"))
	test(getComptesComunnes("A","2014"), "Colonne A, Année 2014 : 2 365")
	# print(getComptesComunnes("B","2013"))
	test(getComptesComunnes("B","2013"), "Colonne B, Année 2013 : 2 235")
	# print(getComptesComunnes("C","2012"))
	test(getComptesComunnes("C","2012"), "Colonne C, Année 2012 : 1 085")
	# print(getComptesComunnes("D","2010"))
	test(getComptesComunnes("D","2010"), "Colonne D, Année 2010 : 1 265")

	# Mauvais test
	# print(getComptesComunnes("C","2004"))
	test(getComptesComunnes("C","2004"), "Colonne ou Année non disponible")
	# print(getComptesComunnes("F","2010"))
	test(getComptesComunnes("F","2010"), "Colonne ou Année non disponible")
	# print(getComptesComunnes("E","2001"))
	test(getComptesComunnes("E","2001"), "Colonne ou Année non disponible")



main()

  

