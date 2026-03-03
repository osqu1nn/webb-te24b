pot = (input("5 hela tal seperade med mellanslag"))
skr = pot.split()
y = 0
med = []
print(skr)

if len(skr) > 5:
    raise Exception("för många heltal")
elif len(skr) < 5:
    raise Exception("för lite heltal")

x = [int(i) for i in skr]
print(max(x), "största")
print(min(x), "minsta")

y = sum(x) / len(x)
print(y, "medelvärdet")

for k in x:
    if k > y:
        med.append(k)

print(med)