jewels = "z"
stones = "ZZ"
count = 0

for each_jewel in jewels:
    for each_stone in stones:
        if each_stone == each_jewel:
            count += 1

print(count)