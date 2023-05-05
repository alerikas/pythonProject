'''Paarašyti testų programą:

Testą gali sudaryti bet kiek klausimų
Kiekvienas klausimas gali turėti lygiai 3 atsakymus. Tik vienas iš jų yra teisingas.
Kiekvienas klausimas turi po 1 tašką. Jei atsakymas teisingas, prie balų sumos pridedamas tas 1 taškas.
Naudotojui parodomas klausimas, kuris atspausdinamas “command line”, naudotojui turi įvesti atsakymo numerį (arba trumpą atsakymą).
Kai naudotojas atsako į visus klausimus, jam parodoma, į kiek klausimų atsakyta teisingai. '''


klausimai = [
    { "klausimas": "Kiek Europoje yra saliu?",
      "pasirinkimai": ["A. 50, B. 52, C. 55"],
      "atsakymas": "B"
    }
]
'''pirmas_kl = "Kiek Europoje yra saliu?",
pirmas_ats = '50, 52, 55'
antras_kl = "Kokia yra zemes forma?",
trecias_kl = "Kiek spalvu sudaro vaivorykste",
ketvirtas_kl = "Koks zymiausias L. Davincio paveikslas",
penktas_kl = "Kur randasi Viktorijos Krioklys",
sestas_kl = "Kokioje laiko zonoje gyvename?",
septintas_kl = "Kokia yra Lietuvos sostine?",
astuntas_kl = "Kokie dabar metai?",
devintas_kl = "Koks labiausiai paplites tikejimas?",
desimtas_kl = "Kurios salies kompanyja yra Ferrari?"'''

def klausimo_uzklausimas(klausimas):
    print(klausimas['klausimas'])
    for atsakymas in klausimas["pasirinkimai"]:
        print(atsakymas)
    vartotojo_atsakymas = input("Iveskite atsakymo numeri: ")
    if vartotojo_atsakymas == klausimas["atsakymas"]:
        print("atsakymas teisingas")


