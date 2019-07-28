abc = "abcdefghijklmnopqrstuvwxyz"

def place(string, x):
    n=0
    places = []
    for num in string:
        if num == x: places.append(n)
        n += 1
    return places

string = input("write the expression here: \n")

allplaces = []

for char in abc:
    mult = 0
    newstring = string
    if char in string:
        print(char + ": " + str(place(string, char)))
        for place in place(string, char):
            if place == 0:
                mult += 1
            else:
                mult += int(newstring[:place])
                newstring = string[place+1:]
        print(mult)
