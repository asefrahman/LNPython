nums = [1,2,3]

count = 0

for num in range(len(nums)):
    for num2 in range(num+1, len(nums)):
        if nums[num] == nums[num2]:
            count += 1
print(count)