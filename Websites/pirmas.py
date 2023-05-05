from bs4 import BeautifulSoup
import requests

web = "http://www.meteo.lt/"

svetaine = requests.get('http://www.meteo.lt/')
svetaines_kodas = svetaine.text

svetaine_2 = BeautifulSoup(svetaines_kodas, 'html.parser')
miestai = svetaine_2.find_all( "tr", "town_list" )

uzklausa_miestas= input("Iveskite kokio miesto oru norite: Vilnius, Kaunas, Klaipeda, Siauliai, Panevezys ")

if uzklausa_miestas == "Kaunas":
    for miestas in miestai:
        if miestas.find("a", href= "/lt/miestas?placeCode=Kaunas") == None:
            continue
        print(miestas.get_text().strip() )

if uzklausa_miestas == "Vilnius":
    for miestas in miestai:
        if miestas.find("a", href= "/lt/miestas?placeCode=Vilnius") == None:
            continue
        print(miestas.get_text().strip() )

if uzklausa_miestas == "Panevezys":
    for miestas in miestai:
        if miestas.find("a", href= "/lt/miestas?placeCode=Panevezys") == None:
            continue
        print(miestas.get_text().strip() )

if uzklausa_miestas == "Siauliai":
    for miestas in miestai:
        if miestas.find("a", href= "/lt/miestas?placeCode=Siauliai") == None:
            continue
        print(miestas.get_text().strip() )

if uzklausa_miestas == "Klaipeda":
    for miestas in miestai:
        if miestas.find("a", href= "/lt/miestas?placeCode=Klaipeda") == None:
            continue
        print(miestas.get_text().strip() )ac






