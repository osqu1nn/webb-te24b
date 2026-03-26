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

p = input("What are you choosing sten, sax, pase?").lower()

if p == "sten" or "sax" or "pase":
    stepa()
    print("ai valde", b)
    solve(b, p)
