import functools
from functools import reduce

skaiciai = [1,2,3,4,5]

"""def sumuok (x, y):
    print(f"Skaiciuoju x: {x} ir y: {y}")
    return x+y+1

mod_skaiciai = reduce (sumuok, skaiciai)
print(mod_skaiciai)

t = "Labas"
t2 = "Rytas"
print(t + t2)"""

sarasas = ["Labas", 2, 3, "Rytas", False, True, True, True, False]
tik_zodziai = list(filter(lambda el: type (el)==str, sarasas))
print(tik_zodziai)
zodis = " ".join(tik_zodziai)
print(zodis)

def sudek_zodzius (pirmas, antras):
    return pirmas + " " + antras
zodis = reduce(sudek_zodzius, tik_zodziai)
zodis = reduce(lambda pirmas, antras: pirmas + " " + antras, tik_zodziai)
print(zodis)

booleon = list(filter(lambda sk: type(sk) == bool, sarasas))
print(booleon)
print(sum(booleon))



