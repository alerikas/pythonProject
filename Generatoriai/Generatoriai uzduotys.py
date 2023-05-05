# Parašykite generatorių, kuris kaskartą inicijuotas su funkcija next grąžintų
# sekantį porinį skaičių. Pirmas sk. 2, toliau 4 ir taip be pabaigos.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a,b =b, a+b

seka = fibonacci()
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))
print(next(seka))



