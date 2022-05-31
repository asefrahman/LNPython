nums = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = nums[0]

recent_sum = 0
for num in nums:
    recent_sum += num
    print("recent_sum:",recent_sum)
    if recent_sum > max_sum:
        max_sum = recent_sum
        print("max_sum:", max_sum)

    if recent_sum < 0:
        recent_sum = 0

print(max_sum)
