from typing import List, Any

nums = [2, 3, 4]
newnumlist = []
sum = 0
i = 0
for num in nums:
    sum = sum + num
    newnumlist[i] = sum
    i+= 1
# return nums
print(newnumlist)
