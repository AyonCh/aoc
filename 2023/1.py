try:
    ans1 = 0
    ans2 = 0
    while True:
        string = input()
        num1 = 0
        num2 = 0
        data = {}
        nums = ["one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine"]
        for i in range(len(string)):
            if string[i].isnumeric() and num1 == 0:
                num1 = string[i]
            if string[len(string)-1-i].isnumeric() and num2 == 0:
                num2 = string[len(string)-1-i]

            if string[i].isnumeric():
                data[i] = string[i]

        for x in nums:
            if x in string:
                data[string.find(x)] = str(nums.index(x)+1)

        ans1 += int(str(num1) + str(num2))
        ans2 += int(data[min(data)] + data[max(data)])
except:
    print(f"\nPart 1: {ans1}")
    print(f"Part 2: {ans2}")
