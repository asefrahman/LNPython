operations = ["--X", "X++", "X++"]
sum = 0
i = 0
for index in operations:
    if operations[i] == "--X" or operations[i] == "X--":
        sum -= 1
    if operations[i] == "++X" or operations[i] == "X++":
        sum += 1
    i+= 1
print(sum)