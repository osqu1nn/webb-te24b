import random

def stepa():
    lap = ["sten", "sax", "pase"]
    return random.choice(lap)

b = stepa()

def solve(b, p):
    if b == p:
        print("oavgjort")
    elif p == "pase" and b == "sten" or \
        (p == "sax" and b == "pase") or \
        (p == "sten" and b == "sax"):
        print("du vann")
    else:
        print("ai vann")

p = input("What are you choosing sten, sax, pase?")

if p == "sten":
    stepa()
    print("ai valde", b)
    solve(b, p)
elif p == "sax":
    stepa()
    print("ai valde", b)
    solve(b, p)
elif p == "pase":
    stepa()
    print("ai valde", b)
    solve(b, p)