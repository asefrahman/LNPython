nums = [8, 1, 2, 2, 3]
newlist = []
for num in nums:
    count = 0
    for num2 in nums:
      if num2 < num:
          count+= 1
    newlist.append(count)

print(newlist)
