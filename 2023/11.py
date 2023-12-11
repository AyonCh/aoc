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
                data.append([x,y])
        dat.append(a)
        y += 1
except:
    ans = 0
    for x in range(len(data)):
        for y in data[x+1:]:
            ans += abs(data[x][0] - y[0]) + abs(data[x][1] - y[1]))
    print(ans)