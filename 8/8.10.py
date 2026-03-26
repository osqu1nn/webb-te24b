def storsta(sekvens):
    # Om sekvensen är tom
    if len(sekvens) == 0:
        return None

    # Om sekvensen har ett element
    if len(sekvens) == 1:
        return sekvens[0]

    # Ta sista elementet
    sista = sekvens[-1]

    # Hitta största i resten av sekvensen
    storst_i_rest = storsta(sekvens[:-1])

    # Jämför och returnera det största
    if storst_i_rest > sista:
        return storst_i_rest
    else:
        return sista


# Test
tal = [3, 8, 2, 10, 5]
print("Största talet:", storsta(tal))