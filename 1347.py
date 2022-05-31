s = "anagram"
t = "mangaar"
string_to_add = ""
result = 0
count = 0
temp = ""
for char in s:
    if char not in t:
        string_to_add = string_to_add + char
        result += 1
    elif char in t and count > 0:
        if char in string_to_add:
            string_to_add = string_to_add + char
            count += 1
            result += 1
        else:
            string_to_add = string_to_add + char
            count -= 1
            result += 1
    else:
        t = t.replace(char, '', 1)
        print(t)
        count += 1

print(string_to_add, result)