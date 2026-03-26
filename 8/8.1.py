import math

def berakna_omkrets(rad):
    return 2 * math.pi * rad

def berakna_area(rad):
    return math.pi * rad ** 2

radie = float(input("Ange radien på cirkeln: "))

omkrets = berakna_omkrets(radie)
area = berakna_area(radie)

print(f"Omkretsen är: {omkrets}")
print(f"Arean är: {area}")