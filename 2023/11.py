try:
    data = []
    dat = []
    y = 0
    while True:
        i = input()
        a = []
        for x in range(len(i)):
            a.append(i[x])
            if i[x] == "#":
                data.append([x, y])
        dat.append(a)
        y += 1
except:
    ans = 0
    ans1 = 0
    row = []
    col = []
    cols = list(map(list, zip(*dat)))
    for x in range(len(dat)):
        if dat[x].count(".") == len(dat[x]):
            row.append(x)
    for x in range(len(cols)):
        if cols[x].count(".") == len(cols[x]):
            col.append(x)
    for x in range(len(data)):
        for y in data[x+1:]:
            ans += abs(data[x][0] - y[0]) + abs(data[x][1] - y[1])
            ans1 += abs(data[x][0] - y[0]) + abs(data[x][1] - y[1])
            for z in col:
                if max(data[x][0], y[0]) > z and min(data[x][0], y[0]) < z:
                    ans += 1
                    ans1 += 999999
            for z in row:
                if max(data[x][1], y[1]) > z and min(data[x][1], y[1]) < z:
                    ans += 1
                    ans1 += 999999

    print(f"\nPart 1: {ans}")
    print(f"Part 2: {ans1}")
