nums = [2, 7, 11, 15]
target = 9

for digit in range(0, len(nums)):
    for digit2 in range((digit+1), len(nums)):
        if nums[digit] + nums [digit2] == target:
            print(f"[{digit},{digit2}]")
            break
