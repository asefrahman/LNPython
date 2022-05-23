prices = [3,2,6,5,0,3]
lowest= prices[0]
highest = 0
index =0
profit = 0
for price in range(0, len(prices)-1):
    index += 1
    if prices[price] <= lowest:
        lowest = prices[price]
        print("lowest: ",lowest)
    print("index:", index)
for price2 in range(index, len(prices)):
    if prices[price2] > highest:
        highest = prices[price2]
        print("Highest: ", str(highest))


if (highest <= lowest):
    profit = 0
else:
    profit = highest - lowest

print(index)
print (highest, lowest,profit)