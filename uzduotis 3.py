pirmas_skaicius = (input ("iveskite pirma skaiciu:"))
a = float(pirmas_skaicius)
antras_skaicius = (input ("iveskite antra skaiciu:"))
b = float(antras_skaicius)
matematinis_veiksmas = input ("matematinis veiksmas (+, -, /, *, **):")
if matematinis_veiksmas == "+":
    print("skaiciu suma lygi:", a+b)
elif matematinis_veiksmas == "-":
    print("skaiciu suma lygi:", a-b)
elif matematinis_veiksmas == "/":
    print("skaiciu suma lygi:", a/b)
elif matematinis_veiksmas == "*":
    print("skaiciu suma lygi:", a*b)
elif matematinis_veiksmas == "**":
    print("skaiciu suma lygi:", a**b)