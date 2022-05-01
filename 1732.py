gain = [-4,-3,-2,-1,4,3,2]
#gain = [-5, 1, 5, 0, -7]
#altitude = [0, -5, -4, 1, 1, -6]
#Solution 1
highest = 0
current = 0
for change in gain:
    current += change
    if (current > highest):
        highest = current
print(highest)
#Solution 2
current1 = 0
alt = [0]
for change in gain:
    current1 += change
    alt.append(current1)

print(alt)

highest1= 0
for num in alt:
    if num > highest1:
        highest1 = num

print(highest1)



