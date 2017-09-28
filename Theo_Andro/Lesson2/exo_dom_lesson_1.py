import requests 
from bs4 import BeautifulSoup

url="http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice="
classename="montantpetit G"
def obtenirDonnees(url,classename):
    for j in range(6):  # on parcourt les six pages pour les comptes de 2010 a 2015
        
        url_b=url+str(2010+j)
        res=requests.get(url_b)  # on lit la page
        
        if res.status_code==200:
            
            soup = BeautifulSoup(res.text, 'html.parser') # lire la page correctement
            
            for i in range(15): # On parcourt les donnees auxquelles on veut acceder 
                
                if (i%3)!=0 and i!=6 and i!=7 and i!=8:   #verifier que l on traite la bonne donnee   
                
                    if (i%3)==1:  
                        if i<3: #Definir la donnee que l on regarde
                            nom_donnees="A"
                        elif i<6 and i>2:
                            nom_donnees="B"
                        elif i>8 and i<12:
                            nom_donnees="C"
                        elif i>11 and i<15:
                            nom_donnees="D"
                            
                        share_content = soup.find_all(class_=classename)[i].text.strip() #on recupere la donnee
                        print("En "+str(2010+j)+"les donnees "+nom_donnees+"  en euros par habitant sont de "+share_content) # on affiche correctement la donnee
                        
                    elif (i%3)==2:
                        if i<3:
                            nom_donnees="A"
                        elif i<6 and i>2:
                            nom_donnees="B"
                        elif i>8 and i<12:
                            nom_donnees="C"
                        elif i>11 and i<15:
                            nom_donnees="D"
                        share_content = soup.find_all(class_=classename)[i].text.strip()
                        print("En "+str(2010+j)+"les donnees "+nom_donnees+" la moyenne de la strate est de "+share_content)

