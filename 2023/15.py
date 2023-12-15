with open("2023/inp") as f:
    data = f.read().strip().split(",")


def hash(string):
    temp = 0
    for char in string:
        temp += ord(char)
        temp *= 17
        temp = temp % 256
    return temp


boxs = {}
for x in data:
    if x[-1] == "-":
        y = x[0:-1]
        if hash(y) in boxs and y in boxs[hash(y)]:
            del boxs[hash(y)][y]
    else:
        y = x.split("=")
        if hash(y[0]) in boxs:
            boxs[hash(y[0])][y[0]] = int(y[1])
        else:
            boxs[hash(y[0])] = {y[0]: int(y[1])}

print(f"""Part 1: {sum(map(hash, data))}""")
print(f"""Part 2: {sum(map(sum, [[(x+1) * (y+1) * (boxs[x][z])
      for y, z in enumerate(boxs[x])] for x in boxs]))}""")
