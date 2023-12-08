try:
    instructions = input()
    coords = {}
    while True:
        i = input()
        if i != "":
            coords[i.split(" = ")[0]] = (i.split(" = ")[1][1:-1]).split(", ")

except:
    idx = 0
    key = list(coords.keys())[0]
    while key != "ZZZ":
        dir = instructions[idx % len(instructions)]
        if dir == "R":
            key = coords[key][1]
        if dir == "L":
            key = coords[key][0]
        idx += 1
    print(f"\nPart 1: {idx}")
