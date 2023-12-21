from collections import deque

with open("2023/inp") as f:
    i = f.read().splitlines()

for y in range(len(i)):
    for x in range(len(i[y])):
        if i[y][x] == "S":
            start = (y, x)

q = deque([start])
seen = [start]
steps = -1
while True:
    steps += 1
    l = []
    while q:
        y, x = q.popleft()
        if y < len(i) - 1 and i[y][x] in "S|7F" and i[y+1][x] != "." and (y+1, x) not in seen:
            seen.append((y+1, x))
            l.append((y+1, x))
        if y > 0 and i[y][x] in "S|JL" and i[y-1][x] != "." and (y-1, x) not in seen:
            seen.append((y-1, x))
            l.append((y-1, x))
        if x < len(i[0]) - 1 and i[y][x] in "S-LF" and i[y][x+1] != "." and (y, x+1) not in seen:
            seen.append((y, x+1))
            l.append((y, x+1))
        if x > 0 and i[y][x] in "S-J7" and i[y][x-1] != "." and (y, x-1) not in seen:
            seen.append((y, x-1))
            l.append((y, x-1))
    if l:
        q = deque(l)
    else:
        print(f"Part 1: {steps}")
        break
