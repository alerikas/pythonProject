sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

def ar_skaicius (element):
    print("tikriname elementa: " + str (element))
    print("Tai yra: " + str (type(element)))
    return type (element) is int or type(element) is float

tik_skaiciai = list(filter(ar_skaicius, sarasas))
tik_skaiciai = list(filter(lambda element: type(element) is int or type(element) is float,sarasas))
tik_skaiciai = [element for element in sarasas if type(element) is int or type(element) is float]
print(tik_skaiciai)
print(sum(tik_skaiciai))