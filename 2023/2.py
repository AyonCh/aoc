try:
    ans1 = 0
    ans2 = 0
    while True:
        i = input().split(":")
        id = int(i[0].split(" ")[1])
        sets = i[1].split(";")
        possible = True
        idx = 0
        blue = []
        red = []
        green = []
        while possible and idx < len(sets):
            x = sets[idx]
            for y in x.split(","):
                z = y.strip().split(" ")
                if z[1][0] == "b":
                    if int(z[0]) <= 14:
                        possible = True
                    else:
                        possible = False
                        break
                if z[1][0] == "r":
                    if int(z[0]) <= 12:
                        possible = True
                    else:
                        possible = False
                        break
                if z[1][0] == "g":
                    if int(z[0]) <= 13:
                        possible = True
                    else:
                        possible = False
                        break
            idx += 1
        for x in sets:
            for y in x.split(","):
                z = y.strip().split(" ")
                if z[1][0] == "b":
                    blue.append(int(z[0]))
                if z[1][0] == "r":
                    red.append(int(z[0]))
                if z[1][0] == "g":
                    green.append(int(z[0]))

        if possible:
            ans1 += id
        ans2 += max(blue)*max(red)*max(green)

except:
    print(f"\nPart 1: {ans1}")
    print(f"Part 2: {ans2}")
