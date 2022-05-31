prices = [7, 1, 5, 3, 6, 4]
# new_prices = sorted(prices)
# print(new_prices)
# max = 0
# min = 0
# half_length = len(prices)//2
#
# for i in range(half_length):
#     if prices.index(new_prices[~i]) > prices.index(new_prices[i]):
#         max = new_prices[~i]
#         min = new_prices[i]
#
# print(max, min)

left = 0  # Buy
right = 1  # Sell
max_profit = 0
while right < len(prices):
    currentProfit = prices[right] - prices[left]  # our current Profit
    if prices[left] < prices[right]:
        max_profit = max(currentProfit, max_profit)
    else:
        left = right
    right += 1
print(max_profit)