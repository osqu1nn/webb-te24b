def ar_perfekt(tal):
    summa = 0

    for i in range(1, tal):
        if tal % i == 0:
            summa = summa + i

    if summa == tal:
        return True
    else:
        return False



n = int(input("Skriv in ett tal: "))

if ar_perfekt(n):
    print(n, "är ett perfekt tal")
else:
    print(n, "är inte ett perfekt tal")