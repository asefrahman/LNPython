candies = [2,3,5,1,3]
extraCandies = 3
result = []

for kid in candies:
    greatest = True
    for kid2 in candies:
        if kid2 > kid+extraCandies:
            greatest = False
            break
    result.append(greatest)



print(result)