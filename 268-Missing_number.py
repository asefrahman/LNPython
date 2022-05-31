nums = [1,2]
nums.sort()
missed_number = len(nums)

for i in range(0,len(nums)):
    if i != nums[i]:
        print("i: ", i, "nums[i]: ", nums[i] )
        missed_number = i
        print("asnwer:",missed_number)
print(missed_number)