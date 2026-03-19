Antal = 1

def lon(antal):
    print(antal, "years")
    if antal == 1:
        sist = 25000
        print(sist)
    else:
        sist = 25000 * 1.03 ** antal + (900 * antal)
        print(sist)
    return sist

lon(antal=Antal)
