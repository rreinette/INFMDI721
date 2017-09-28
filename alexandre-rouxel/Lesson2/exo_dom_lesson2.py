#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:28:54 2017

@author: alexandre rouxel
"""
import requests
import numpy as np
from bs4 import BeautifulSoup
import unittest
import pandas as pd

#Le code doit utiliser le css tr:nth-of-type() 

def getSoupFromURL(year) : 
    
    if int(year) >= 2010 and int(year) <= 2015 :
        url = 'http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=' + str(year)

    else : 
        return False 
    res = requests.get(url)
    
    if res.status_code == 200:
       soup = BeautifulSoup(res.text, 'html.parser')
       return soup
    else :
       return None

def getTableIndex(Letter,Soup) :
    
    if Letter == 'A' :
        DefRaw = 'TOTAL DES PRODUITS DE FONCTIONNEMENT = A'
    elif Letter == 'B' :
        DefRaw = 'TOTAL DES CHARGES DE FONCTIONNEMENT = B'
    elif Letter == 'C' :
        DefRaw = "TOTAL DES RESSOURCES D'INVESTISSEMENT = C"
    elif Letter == 'D' :
        DefRaw = "TOTAL DES EMPLOIS D'INVESTISSEMENT = D"
    else : 
        return False
    
    DefCellule1 = 'Euros par habitant'
    
     # recherche de l'indice de la ligne
    Rows = Soup.find_all ( 'tr' )
    TextRow = Soup.find ( 'td' , text=DefRaw).parent
    RowIdx = Rows.index(TextRow) +1 
    
    # recherche de l'indice de la cellule 
    TextCel = Soup.find('th',text=DefCellule1 ).parent
    idx=0
    for el in str(TextCel).split('<th') : 
        if el.find(DefCellule1) > 0 : 
            break
        idx += 1
    ColIdx = idx
    
    #la cellule 1 est toujours suivie de la cellule 2 telle que définie
    #DefCellule2 = 'Moyenne de la strate'

    return ( RowIdx , ColIdx )
    
def getCelluleValue(RowIdx,ColIdx,Soup) :
    
    #lecture de la cellule dans la linge
    outRow = Soup.select("tr:nth-of-type({})".format(RowIdx))
    outCell1 = outRow[0].select("td:nth-of-type({})".format(ColIdx))
    outCell2 = outRow[0].select("td:nth-of-type({})".format(ColIdx+1))
    valCell1 = outCell1[0].text.replace(" ", "")
    valCell2 = outCell2[0].text.replace(" ", "")
    
    return (valCell1,valCell2)
    
def getTabValues(Letter,year) :    

    Soup = getSoupFromURL(year)
    RowIdx , ColIdx  = getTableIndex(Letter,Soup)
   
    #lecture de la cellule 1 
    A = getCelluleValue(RowIdx,ColIdx,Soup)
    #lecture de la cellule suivante
    #A2 = getCelluleValue(RowIdx,ColIdx+1,Soup)

    return(list(map(int,A)))

    
def getMatrixValues(TabLetter,TabYears) :
    
    nb_col = len(TabLetter.split(' ')*2);
    nb_row = len(TabYears.split(' '))
    Matrix = np.zeros((nb_row,nb_col),np.int32);

    for year_idx,Year in enumerate(TabYears.split(' ')) :
         for letter_idx,Letter in enumerate(TabLetter.split(' ')) :
            out=getTabValues(Letter,Year)
            Matrix[year_idx,2*letter_idx:2*letter_idx+2:1]=out
    return(Matrix)
            
def test_case () :
    
    TabLetter = 'A B C D'
    TabYears  = '2010 2011 2012 2013 2014'
    Matrix = getMatrixValues(TabLetter,TabYears)
   
    TabLetter = 'A1 A2 B1 B2 C1 C2 D1 D2'
    Letters=TabLetter.split(' ')
    Years=TabYears.split(' ')
    df = pd.DataFrame(Matrix,index=Years, columns = Letters)
    print('-------')
    print('X1 = Euros par habitant')
    print('X2 = Moyenne de la strate')
    print('-------')
    print(df)
    print('-------')

class Lesson2_Tests(unittest.TestCase):

         
    def testgetTabValuess(self):
        
        self.assertEqual( getTabValues('A','2010') , [2449 , 2449] )
        self.assertEqual( getTabValues('B','2010') , [2241 , 2241] )
        self.assertEqual( getTabValues('C','2010') , [1119 , 1119] )
        self.assertEqual( getTabValues('D','2010') , [1265 , 1265] )
        
        self.assertEqual( getTabValues('A','2012') , [2311 , 2311] )
        self.assertEqual( getTabValues('B','2012') , [2135 , 2135] )
        self.assertEqual( getTabValues('C','2012') , [1085 , 1085] )
        self.assertEqual( getTabValues('D','2012') , [1058 , 1058] )
        
        self.assertEqual( getTabValues('A','2014') , [2365 , 2365] )
        self.assertEqual( getTabValues('B','2014') , [2294 , 2294] )
        self.assertEqual( getTabValues('C','2014') , [1066 , 1066] )
        self.assertEqual( getTabValues('D','2014') , [1048 , 1048] )
    
    
    def main():
        unittest.main()
        
    if __name__ == '__main__':
        main()
    
test_case ()

Lesson2_Tests.main()




        