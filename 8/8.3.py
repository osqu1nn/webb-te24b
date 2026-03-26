def antal_siffror(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
print(antal_siffror(7))
print(antal_siffror(1234))
print(antal_siffror(98765))
