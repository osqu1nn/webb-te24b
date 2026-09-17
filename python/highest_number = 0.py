highest_number = 0
highest_username = ""

with open("personer.txt") as file:
    for line in file:
        username, *number = line.split()
        maximum = max(map(int,number))

        if maximum > highest_number:
            highest_number = maximum
            highest_username = username

print(highest_username, highest_number)
