def nfak(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat = resultat * i
    return resultat


# Test av funktionen
tal = 5
svar = nfak(tal)
print("Fakulteten av", tal, "är", svar)

print("Fakulteten av 3 är", nfak(3))
print("Fakulteten av 7 är", nfak(7))