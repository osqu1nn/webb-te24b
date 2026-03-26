def fyll(lista, start, slut, varde):
    for i in range(start, slut + 1):
        lista[i] = varde



a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

fyll(a, 5, 9, 2.3)

print(a)