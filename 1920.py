nums = [0,2,1,5,3,4]
new_num = []
current_num = 0
for i in range(len(nums)):
    current_num = nums[nums[i]]
    new_num.append(current_num)
print(new_num)

