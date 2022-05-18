s = "textbook"
s_length = len(s)
half_s = int(s_length/2)
s1 = s[0:half_s]
s2 = s[half_s:]
count_s1 = 0
count_s2 = 0
vowels = ['a', 'e', 'i','o','u']
alike = True
for char in s1.lower():
    for char2 in vowels:
        if char == char2:
            count_s1 = count_s1 + 1
for char in s2.lower():
    for char2 in vowels:
        if char == char2:
            count_s2 = count_s2 + 1

if count_s1 != count_s2:
    alike = False

print(count_s1, count_s2)
print(alike)
