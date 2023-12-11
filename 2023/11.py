try:
    data = []
    y = 0
    while True:
        i = input()
        for x in range(len(i)):
            if i[x] == "#":
                data.append([x,y])
        y += 1
except:
    ans = 0
    for x in data:
        for y in data:
            ans += abs(x[0] - y[0]) + abs(x[1] - y[1]))
    print(ans)