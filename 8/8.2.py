import math

def berakna_cirkel(rad):
    omkrets = 2 * math.pi * rad
    area = math.pi * rad ** 2
    return omkrets, area

radie = float(input("Ange radien på cirkeln: "))

omkrets, area = berakna_cirkel(radie)

print(f"Omkretsen är: {omkrets}")
print(f"Arean är: {area}")