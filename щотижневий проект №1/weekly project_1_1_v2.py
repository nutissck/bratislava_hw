def chislo(n):
    suma = 0
    cisla = []
    for i in range(n):
        x = int(input(f"Zadaj {i + 1}. cislo: "))
        cisla.append(str(x))
        suma += x
    return " + ".join(cisla) + f" = {suma}"
n = int(input("кількість чисел -  "))
print(chislo(n))