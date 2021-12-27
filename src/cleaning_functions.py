import re



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


def clean_columnFatal(x):
    """
    Esta función armoniza los valores únicos de la columna "Fatal (Y/N)", reduciéndolos a 3.
    Args: cada uno de los valores de dicha columna (string).
    Return: Y,N,Unkown (string).
    """
    if x == 'Y' or x=='y':
        return "Y"

    elif x == ' N':
        return "N"

    else:
        return "Unknown"


def funcion_valores_unicos(x):
        """
        Esta función devuelve los elementos de la columna "Species" bien como categorías que he creado o bien como "others".

        Args:
        x(string):elemento de la columna "Specie".
    
        Return: El nuevo nombre del elemento:especie/ "Others".
        """
        dicc_especies={
            "White shark":re.search(".*[Ww](hite|HITE).*",str(x)),
            "Tiger shark":re.search(".*[Tt](iger|IGER).*",str(x)),
            "Lemon shark":re.search(".*[Ll](emon|EMON).*",str(x)),
            "Hammerhead shark":re.search(".*[Hh](ammerhead|AMMERHEAD).*",str(x)),
            "Bull shark":re.search(".*[Bb](ull|ULL).*",str(x)),
            "Blue shark":re.search(".*[Bb](lue|LUE).*",str(x)),
            "Silvertip shark":re.search(".*[Ss](ilvertip|ILVERTIP).*",str(x)),
            "Nurse shark":re.search(".*[Nn](urse|URSE).*",str(x)),
            "Whaler shark":re.search(".*[Ww](haler|HALER).*",str(x)),
            "Blacktip shark":re.search(".*[Bb](lacktip|LACKTIP).*",str(x)),
            "Mako shark":re.search(".*[MM](ako|AKO).*",str(x)),
            "Sand shark":re.search(".*[Ss](and|AMD).*",str(x)),
            "Wobbegong shark":re.search(".*[Ww](obbegong|OBBEGONG).*",str(x)),
            "Galapagos shark":re.search(".*[Gg](alapagos|ALAPAGOS).*",str(x)),
            "Grey shark":re.search(".*[Gg](rey|REY).*",str(x)),
            "Leopard shark":re.search(".*[Ll](eopard|EOPARD).*",str(x)),
            "Zambesi shark":re.search(".*[Zz](ambesi|AMBESI).*",str(x)),
            "Blacktail shark":re.search(".*[Bb](lacktail|LACKTAIL).*",str(x)),
            "Red shark":re.search(".*[Rr](ed|ED).*",str(x)),
            "Dusky shark":re.search(".*[Dd](usky|USKY).*",str(x)),
            "Raggedtooth shark":re.search(".*[Rr](aggedtooth|AGGEDTOOTH).*",str(x)),
            "Spinner shark":re.search(".*[Ss](pinner|PINNER).*",str(x)),
            "Cow shark":re.search(".*[Cc](ow|OW).*",str(x)),
            "Porbeagle shark":re.search(".*[Pp](orbeagle|ORBEAGLE).*",str(x)),
            "Caribbean reef shark":re.search(".*[Cc](aribbean|ARIBBEAN).*",str(x)),
            "Sandbar shark":re.search(".*[Ss](and|AND).*",str(x)),
            "Silky shark":re.search(".*[Ss](ilky|ILKY).*",str(x)),
            "Zambezi shark":re.search(".*[Zz](ambezi|AMBEZI).*",str(x)),
            "Sevengill shark":re.search(".*[Ss](evengill|EVENGILL).*",str(x)),
            "Copper shark":re.search(".*[Cc](opper|OPPER).*",str(x)),
            "Angel shark":re.search(".*[Aa](ngel|NGEL)\s",str(x)),
            "Salmon shark":re.search(".*[Ss](almon|ALMON).*",str(x)),
            "Goblin shark":re.search(".*[Gg](oblin|OBLIN).*",str(x)),
            "Thresher shark":re.search(".*[Tt](hresher|HRESHER).*",str(x)),
            "Dogfish shark":re.search(".*[Dd](ogfish|OGFISH).*",str(x)),
            "Involvement not confirmed":re.search("[^.?!]*involvement[^.?!]*",str(x))}
        
        
        for key,values in dicc_especies.items():
            if values:
                return key
        return "Others"



def valores_unicos_activity(x):
    """
    Esta función devuelve los elementos de la columna "Activity" bien como categorías que he creado o bien como "others".
    Args:
    x(string):elemento de la columna "Activity".
    Return: El nuevo nombre del elemento:actividad/ "Others".
    """
    dicc_activity={
            "Fishing":re.search(".*[Ff](ishing|ISHING).*",str(x)),
            "Swimming":re.search(".*[Ss](wimming|WIMMing).*",str(x)),
            "Kite":re.search(".*[Kk](ite|ITE).*",str(x)),
            "Walking":re.search(".*[Ww](alking|ALKING).*",str(x)),
            "Boogie Board":re.search(".*[Bb](oogie|OOGIE).*",str(x)),
            "Body Boarding":re.search(".*[Bb](ody|ODY).*",str(x)),
            "Wind Surfing":re.search(".*[wW](ind|IND).*",str(x)),
            "Boat":re.search(".*[Bb](oat|OAT).*",str(x)),
            "Interact with sharks":re.search(".*[Ss](hark|HARK).*",str(x)),
            "Diving":re.search(".*[Dd](iving|IVING).*",str(x)),
            "Standing in water":re.search(".*[Ss](tand|TAND).*",str(x)),
            "Paddling":re.search(".*[Pp](addl|ADDL).*",str(x)),
            "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
            "OverBoard":re.search(".*[Oo](verb|VERB).*",str(x)),
            "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
            "Floating":re.search(".*[Ff](loat|LOAT).*",str(x)),
            "Jumping":re.search(".*[Jj](ump|UMP).*",str(x))}

    for key,values in dicc_activity.items():
        if values:
            return key
    return "Others"   
    

def valores_unicos_injury (x):
    """
    Esta función devuelve los elementos de la columna "Injury" bien como categorías que he creado o bien como "others".
    Args:
    x(string):elemento de la columna "Injury".
    Return: El nuevo nombre del elemento:injury/ "Others".
    """     
    dicc_injury={
            "No injury":re.search(".*[Nn](o|O)\s*[Ii](njury|NJURY).*",str(x)),
            "Minor Injury":re.search(".*[Mm](inor|INOR)\s*[Ii](njury|NJURY|njuries|NJURIES|ed|ED).*",str(x)),
            "Hand injury":re.search(".*[Hh](and|AND).*",str(x)),
            "Leg injury":re.search(".*[Ll](eg|EG).*",str(x)),
            "Laceration":re.search(".*[Ll](aceration|ACERATION).*",str(x)),
            "Fatal":re.search(".*[Ff](atal|ATAL).*",str(x)),
            "Foot Injury":re.search(".*[Ff](oot|OOT).*",str(x)),
            "Ankle Injury":re.search(".*[Aa](nkle|NKLE).*",str(x)),
            "Shoulder Injury":re.search(".*[Ss](houlder|HOULDER).*",str(x)),
            "Abrasion Injury":re.search(".*[Aa](brasion|BRASION).*",str(x)),
            "Calf Injury":re.search(".*[Cc](alf|ALF).*",str(x)),
            "Torso Injury":re.search(".*[Tt](orso|ORSO).*",str(x)),
            "Feet Injury":re.search(".*[Ff](eet|EET).*",str(x)),
            "Thigh Injury":re.search(".*[Tt](high|HIGH).*",str(x)),
            "Arm injury":re.search(".*[Aa](rm|RM)\s*[Ii](njury|NJURY).*",str(x)),
            "Puncture wounds":re.search(".*[Pp](uncture|UNCTURE)\s*[Ww](ounds|OUNDS).*",str(x)),
            "Knee Injury":re.search(".*[Kk](nee|NEE).*",str(x)),
            "Chest Injury":re.search(".*[Cc](hest|HEST).*",str(x)),
            "Elbow Injury":re.search(".*[Ee](lbow|LBOW).*",str(x))}
        
    for key,values in dicc_injury.items():
        if values:
            return key
    return "Others"


def años(x):
    try:
        return int(x)
    except:
        return x
