import math

try:
    ans = 0
    ans1 = []
    vals = {")": 3, "]": 57, "}": 1197, ">": 25137}
    vals1 = {"(": 1, "[": 2, "{": 3, "<": 4}
    symbols = {"(": ")", "{": "}", "[": "]", "<": ">"}
    while True:
        i = input()
        stack = []
        for char in i:
            if char in "({[<":
                stack.append(char)
            if char in ">]})":
                if len(stack) > 0:
                    if symbols[stack[-1]] == char:
                        stack.pop()
                    else:
                        ans += vals[char]
                        break
                else:
                    ans += vals[char]
                    break
        else:
            temp = 0
            for char in stack[::-1]:
                temp *= 5
                temp += vals1[char]
            ans1.append(temp)
except:
    print(f"\nPart 1: {ans}")
    print(f"Part 2: {sorted(ans1)[math.floor(len(ans1)/2)]}")
