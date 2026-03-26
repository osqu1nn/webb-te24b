def medelvarde(sekvens):
    return sum(sekvens) / len(sekvens)



lista = [2, 4, 6, 8]
tupel = (1, 3, 5, 7, 9)

print("Medelvärde av listan:", medelvarde(lista))
print("Medelvärde av tupeln:", medelvarde(tupel))