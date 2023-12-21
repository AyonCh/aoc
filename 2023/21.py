from collections import deque

with open("2023/inp") as f:
    data = f.read().splitlines()

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = (y, x)
q = deque([start])
steps = 0
while steps < 64:
    steps += 1
    l = []
    while q:
        y, x = q.popleft()
        if data[y][x] in "S.":
            if x < len(data[0]) - 1 and data[y][x+1] != "#":
                l.append((y, x+1))
            if x > 0 and data[y][x-1] != "#":
                l.append((y, x-1))
            if y < len(data) - 1 and data[y+1][x] != "#":
                l.append((y+1, x))
            if y > 0 and data[y-1][x] != "#":
                l.append((y-1, x))
    if l:
        q = deque(l)
    else:
        break
print(f"Part 1: {len(set(q))}")
