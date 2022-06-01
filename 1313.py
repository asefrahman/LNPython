nums =  [1,1,2,3]
n = len(nums)
new_nums=[]
i=0
while i<n:
    to_add = nums[i]* [nums[i+1]]
    new_nums += to_add
    i+=2

print(new_nums)
print([1]*3)