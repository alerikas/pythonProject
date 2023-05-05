from pprint import pprint
import requests
import json

# paimam duomenis iš kačių faktų API
duomenys = requests.get("https://cat-fact.herokuapp.com/facts")

# šie duomenys yra kaip json string, tai reikia juos perkelti į python lists/dictionaries:
kaciu_faktai = json.loads(duomenys.text)


for faktas in kaciu_faktai:
    print(f"Vartotojas {faktas['user']} įkėlė faktą: {faktas['text']}")



# paimam atsitiktinį emoji iš API
emoji_json = requests.get("https://emojihub.yurace.pro/api/random/")


# atspausdiman šio emoji duomenis
print(emoji_json.text)

# emoji duomenis persikeliam į Python žodynus/sąrašus
emoji_duomenys = json.loads(emoji_json.text)

pprint(emoji_duomenys)

print(f"pavadinimas: {emoji_duomenys['name']}")

# spausdimam emoji unicodo numerį
print(f"\{emoji_duomenys['unicode'][0]}")


# padarom, kad mums rodytų patį emoji
# iš unicode kodo atrenkam tik skaičius
emoji_kodas = emoji_duomenys['unicode'][0][2:]

# šiuos skaičius padarom specialiu 16 skaitmenų formatu
emoji_kodas = int(emoji_kodas, 16)

# su chr funkcija surandam šį kodą atitinkantį simbolį, kuris šiuo atveju ir yra mūsų emoji simbolis
emoji = chr(emoji_kodas)
# emoji_kodas = "\\" + emoji_kodas.replace("+", "000")

# spausdinam patį emoji sinbolį
print(emoji)