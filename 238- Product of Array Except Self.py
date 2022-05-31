nums = [1,2,3,4]

new_num = []

for digit in range(len(nums)):
    current_num = 1
    print(nums[digit])
    nums.remove(nums[digit])
    print(nums)
for digit2 in nums:
    current_num = current_num * digit2
new_num.append(current_num)
    # nums.insert(digit, nums[digit])

print(new_num)