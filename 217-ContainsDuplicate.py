nums = [1,2,3,1]
duplicate = False
for digit in range(len(nums)):
    for digit2 in range(digit, len(nums)):
        if digit != digit2:
            if nums[digit] == nums[digit2]:
                duplicate = True

print(duplicate)