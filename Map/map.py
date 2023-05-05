"""def kelti_skaiciu_kvadratu(x):
    return x ** 2

skaiciai = [1,2,3,4,5,6,7,8,9,10]

skaiciai_kv = list(map(kelti_skaiciu_kvadratu, skaiciai))

print(skaiciai_kv)"""

"""skaiciai = [1,2,3,4,5,6,7,8,9,10]
skaiciai_kv = list(map(lambda x: x**2, skaiciai))
print(skaiciai_kv)"""

sakinys = "The Zen Of Python".split()
print(sakinys)
pakeista = list(map(lambda x: x+"!",sakinys))
print(pakeista)
naujas = " ".join(pakeista)
print(naujas)