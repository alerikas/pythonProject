def generacija (n):
    for i in range (n):
        yield i

skaiciu_generatorius = generacija(5)
print(next(skaiciu_generatorius))
print(next(skaiciu_generatorius))
skaiciai = list (skaiciu_generatorius)
print(skaiciai)


