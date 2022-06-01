nums = [2,5,1,3,4,7]
n = 3
new_nums = []

for i in range(int(len(nums)/2)):
    new_nums.append(nums[i])
    new_nums.append(nums[i+n])

print(new_nums)
