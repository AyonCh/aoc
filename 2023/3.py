try:
    data = []
    while True:
        data.append(input())
except:
    ans = []
    for x in range(len(data)):
        prev = ""
        prev1 = ""
        prev2 = ""
        prev3 = ""
        yes = False
        yes1 = False
        yes2 = False
        for y in range(len(data[x])):
            if data[x][y].isnumeric():
                prev2 += data[x][y]
                if yes2:
                    prev3 += data[x][y]
                if x+1 < len(data):
                    if y + 1 < len(data):
                        if not data[x+1][y+1].isnumeric() and data[x+1][y+1] != ".":
                            yes = True
                    if y - 1 > -1:
                        if not data[x+1][y-1].isnumeric() and data[x+1][y-1] != ".":
                            yes = True
                    prev += data[x][y]

                if x-1 > -1:
                    if y + 1 < len(data):
                        if not data[x-1][y+1].isnumeric() and data[x-1][y+1] != ".":
                            yes1 = True
                    if y - 1 > -1:
                        if not data[x-1][y-1].isnumeric() and data[x-1][y-1] != ".":
                            yes1 = True
                    prev1 += data[x][y]
                if y + 1 < len(data):
                    if not data[x][y+1].isnumeric() and data[x][y+1] != ".":
                        ans.append(int(prev))
            else:
                if yes:
                    ans.append(int(prev))
                if yes1:
                    ans.append(int(prev1))
                if yes2 and len(prev2) > 0:
                    ans.append(int(prev2))

                yes = False
                yes1 = False
                yes2 = False
                prev = ""
                prev1 = ""
                prev2 = ""
                if not data[x][y].isnumeric() and data[x][y] != ".":
                    yes2 = True
    print(f"\nPart 1: {sum(set(ans))}")
