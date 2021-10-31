import pandas as pd
import numpy as np
import seaborn as sb



def hemisferio (x):
        """
        Esta función devuelve el hemisferio donde se encuentra un país.

        Args:
        x(string):país.
    
        Return: El hemisferio.
        """
        
        south = ["Angola", "Argentina", "Australia", "Bolivia", "Botswana", "Brazil", "Burundi", "Chile", "Colombia", "Comoros", "Ecuador", "Fiji" , "Gabon", "Equatorial Guinea", "Indonesia", "Solomon Islands", "Kenya", "Kiribati", "Lesotho", "Madagascar", "Malawi", "Maldives", "Mauritius", "Mozambique" , "Namibia", "Nauru", "New Zealand", "Papua New Guinea", "Paraguay", "Peru", "Republic of the Congo", "Democratic Republic of the Congo", "Rwanda", "Samoa", " Sao Tome and Principe "," Seychelles "," Somalia "," Swaziland "," South Africa "," Tanzania "," East Timor "," Tonga "," Tuvalu "," UgandaUruguay "," Vanuatu "," Zambia " ,"Zimbabwe"]
        south_upper=[]
        for i in range(len(south)):
            (south_upper.append(south[i].upper()))
        

        if x in south_upper:
            return "Hemisferio sur"
        else:
            return "Hemisferio norte"



def sustituir (s,b):
    """
        Esta función devuelve la lista de mayor tamaño con los valores que coinciden con la lista de menor tamaño remplazados por "unkown".

        Args:
        small(list):lista menor.
        big(list): lista mayor
    
        Return: La lista de mayor tamaño con los valores que coinciden con la lista de menor tamaño remplazados por "unkown".
        """

    for i,p in enumerate(s):
        if p in b:
                b[i]="unkown"
    return b


        
    

        
 
        


