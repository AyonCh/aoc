try:
    data = {}
    idx = 0
    while True:
        i = input()
        for x in range(len(i)):
            data[(idx, x)] = i[x]
        idx += 1
except:
    prev = ""
    prev1 = ""
    yes1 = False
    yes = False
    yes2 = False
    ans = []
    maxx, maxy = max(data)
    for (x, y) in data:
        if data[(x, y)] == ".":
            if yes:
                ans.append(int(prev))
            if yes1:
                ans.append(int(prev1))
            if yes2:
                ans.append(int(prev))
            prev = ""
            prev1 = ""
            yes1 = False
            yes2 = False
            yes = False
        else:
            if yes1 and data[(x, y)].isnumeric():
                prev1 += data[(x, y)]

            if data[(x, y)].isnumeric():
                prev += data[(x, y)]
            if y+1 <= maxy:
                if data[(x, y)].isnumeric() and not data[(x, y+1)].isnumeric() and data[(x, y+1)] != ".":
                    ans.append(int(prev))
                if not data[(x, y)].isnumeric() and data[(x, y)] != "." and data[(x, y+1)] != ".":
                    yes1 = True
                if x+1 <= maxx and data[(x, y)].isnumeric():
                    if y-1 >= 0 and not data[(x+1, y-1)].isnumeric() and data[(x+1, y-1)] != ".":
                        yes = True
                    if not data[(x+1, y+1)].isnumeric() and data[(x+1, y+1)] != ".":
                        yes = True
                    if not data[(x+1, y)].isnumeric() and data[(x+1, y)] != ".":
                        yes = True

                if x-1 >= 0 and data[(x, y)].isnumeric():
                    if y-1 >= 0 and not data[(x-1, y-1)].isnumeric() and data[(x-1, y-1)] != ".":
                        yes2 = True
                    if not data[(x-1, y+1)].isnumeric() and data[(x-1, y+1)] != ".":
                        yes2 = True
                    if not data[(x-1, y)].isnumeric() and data[(x-1, y)] != ".":
                        yes2 = True
    print(f"\nPart 1: {sum(ans)}")
