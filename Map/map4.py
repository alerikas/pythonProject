skaiciai = [13,25,34,43,25,6,7,8,9,10]

def kriterijus (skaicius):
    print(f"Kriterijus {skaicius}")
    return skaicius % 10

rusiuoti_skaiciai = sorted(skaiciai, key=kriterijus)
print(rusiuoti_skaiciai)