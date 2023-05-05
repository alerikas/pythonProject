import logging

logging.basicConfig(
    filename="skaiciuotuvas.log",
    encoding="UTF-8",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(module)s:%(lineno)d:%(message)s"
)

while True:
    try:
        skaicius = float(input("Iveskite norima skaiciu: "))
        veiksmas = input("Iveskite koki veiksma norite atlikti: ")
        skaicius2 = float(input("Iveskite norima skaiciu: "))
        break
    except ValueError:
        logging.critical("Zmogus ievede klaidinga skaiciu arba simboli")
        exit("Ivestas netinkamas skaicius")

logging.debug(f"Zmogelis pasirinko {veiksmas}")


if veiksmas == "*":
    print("Suma yra: ",skaicius*skaicius2)
elif veiksmas == "**":
    print("Suma yra: ",skaicius**skaicius2)
elif veiksmas == "+":
    print("Suma yra: ",skaicius+skaicius2)
elif veiksmas == "-":
    print("Suma yra: ",skaicius-skaicius2)
elif veiksmas == "/":
    print("Suma yra: ",skaicius/skaicius2)
else: exit("Ivestas netinkamas veiksmas")

