def ref_demo(a, x):
    return sum([e for e in a if e >= x])
#exempel på en lista
lista = [2, 5, 8, 1, 10]
print(ref_demo(lista, 5))