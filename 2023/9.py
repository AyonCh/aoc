try:
  ans, ans1 = 0, 0
  while True:
    i = list(map(int, input().split(" ")))]
    values, values1 = [i],[i[::-1]]
    change, change1 = 0, 0
    while True:
      temp = []
      for x in range(len(values[-1]) - 1):
        temp.append(values[-1][x+1] - values[-1][x])
      values.append(temp)
      if len(values[-1]) == values[-1].count(0):
        break
    for x in values[::-1]:
      change += x[-1]
    while True:
      temp = []
      for x in range(len(values1[-1]) - 1):
        temp.append(values1[-1][x+1] - values1[-1][x])
      values1.append(temp)
      if len(values1[-1]) == values1[-1].count(0):
        break
    for x in values1[::-1]:
      change1 += x[-1]
    ans += change
    ans1 += change1
except:
  print(f"\nPart 1: {ans}")
  print(f"Part 2: {ans1}")