try:
    ans = 0
    ans1 = 0
    data = {}
    while True:
        i = input().split(":")
        id = int(i[0].split(" ")[-1])
        win, card = list(
            map(lambda x: [y for y in x.split(" ") if y], i[1].strip().split(" | ")))
        x = len([1 for x in card if x in win])
        ans += 2**(x-1) if x > 0 else 0
        for y in range(x+1):
            if id+y in data:
                data[id+y] = data[id+y] + 1
            else:
                data[id+y] = 1

        for _ in range(data[id]-1):
            for y in range(1, x+1):
                data[id+y] += 1
except:
    for x in data:
        ans1 += data[x]
    print(f"\nPart 1: {ans}")
    print(f"Part 2: {ans1}")
