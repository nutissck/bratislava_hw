def fibonacci_medzi(od, do):
    a, b = 0, 1
    vysledok = []
    for i in range(do):
        if i >= od:
            vysledok.append(str(a))
        a, b = b, a + b
    return " ".join(vysledok)

print(fibonacci_medzi(0, 6))
print(fibonacci_medzi(10, 14))
print(fibonacci_medzi(100, 101))