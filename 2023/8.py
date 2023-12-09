import math
try:
    instructions = input()
    coords = {}
    a = []
    while True:
        i = input()
        if i != "":
            coords[i.split(" = ")[0]] = (i.split(" = ")[1][1:-1]).split(", ")
            if i.split(" = ")[0][-1] == "A":
              a.append(i.split(" = ")[0])

except:
    idx = 0
    idxs = []
    key = "AAA"
    while key != "ZZZ":
        dir = instructions[idx % len(instructions)]
        if dir == "R":
            key = coords[key][1]
        if dir == "L":
            key = coords[key][0]
        idx += 1
    for x in a:
        k = x
        j = 0
        while k[-1] != "Z":
          dir = instructions[j % len(instructions)]
          if dir == "R":
            k = coords[k][1]
          if dir == "L":
            k = coords[k][0]
          j += 1
        idxs.append(j)
      
    print(f"\nPart 1: {idx}")
    print(f"Part 2: {math.lcm(idxs)}")
