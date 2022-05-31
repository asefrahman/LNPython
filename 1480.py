nums = [1,1,1,1,1]
runningSum = []
current_sum = 0

for num in nums:
    current_sum += num
    runningSum.append(current_sum)

print(runningSum)