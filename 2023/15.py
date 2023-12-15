# i = input()
# ans = 0
# temp = 0
# for x in i:
#     if x == ",":
#         ans += temp
#         temp = 0
#     else:
#         temp += ord(x)
#         temp *= 17
#         temp = temp % 256
# print(f"Part 1: {ans+temp}")
with open("2023/inp") as f:
    data = f.read().strip()
    ans = 0
    temp = 0
    for x in data:
        if x == ",":
            ans += temp
            temp = 0
        else:
            temp += ord(x)
            temp *= 17
            temp = temp % 256
    print(ans+temp)
