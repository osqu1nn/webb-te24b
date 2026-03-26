while True:

    def solve(p2, p1):
        if p2 == p1:
            print("oavgjort")
        elif (p1 == "pase" and p2 == "sten") or \
             (p1 == "sax" and p2 == "pase") or \
             (p1 == "sten" and p2 == "sax"):
            print("spelare 1 vann")
        else:
            print("spelare 2 vann")


    p1 = input("välj sax, sten eller pase p1: ").lower()
    p2 = input("välj sax, sten eller pase p2: ").lower()


    if p1 in ["sten", "sax", "pase"] and p2 in ["sten", "sax", "pase"]:
        solve(p2, p1)
    else:
        print("fel input")
        continue

    again = input("spela igen? (y/n): ").lower()
    if again != "y":
        print("hejdå")
        break