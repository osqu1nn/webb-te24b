tal_lista = list(map(int, input("Skriv in heltal separerade med mellanslag: ").split()))

def ar_udda(tal):
    return tal % 2 != 0

udda_tal = list(filter(ar_udda, tal_lista))

print("Udda tal (med funktion):", udda_tal)

udda_tal_lambda = list(filter(lambda x: x % 2 != 0, tal_lista))

print("Udda tal (med lambda):", udda_tal_lambda)