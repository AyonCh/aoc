try:
  ans = 0
  while True:
    values = [list(map(int, input().split(" ")))]
    change = 0
    while True:
      temp = []
      for x in range(len(values[-1]) - 1):
        temp.append(values[-1][x+1] - values[-1][x])
      values.append(temp)
      if len(values[-1]) == values[-1].count(0):
        break
    for x in values[::-1]:
      change += x[-1]
    ans += change
except:
  print(f"\nPart 1: {ans}")