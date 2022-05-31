accounts = [[2,8,7],[7,1,3],[1,9,5]]
new_accounts = []

for i in range(len(accounts)):
    current_sum = 0
    for j in range(len(accounts[i])):
        current_sum += accounts[i][j]
    new_accounts.append(current_sum)
max_sum = new_accounts[1]
for num in new_accounts:
    if num >= max_sum:
        max_sum = num

print(max_sum)
print(max(new_accounts))

