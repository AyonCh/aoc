t, d = [x.strip() for x in input().split(" ")[1:] if x], [x.strip()
                                                          for x in input().split(" ")[1:] if x]
t1, d1 = "", ""
ans = 1
ans1 = 0
for x in range(len(t)):
    t1 += t[x]
    d1 += d[x]
    a = 0
    for y in range(int(t[x]) + 1):
        if y * (int(t[x]) - y) > int(d[x]):
            a += 1
    ans *= a
for x in range(int(t1) + 1):
    if x * (int(t1) - x) > int(d1):
        ans1 += 1
print(f"Part 1: {ans}")
print(f"Part 2: {ans1}")
