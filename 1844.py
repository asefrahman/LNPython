s = "a1c1e1f"
letter = 0
result = 0
for index in range(len(s)):
    if index % 2 == 0:
        result = ord(s[index])
    if index%2 != 0:
        num = int(s[index])
        letter = chr(result+num)
        s = s.replace(s[index],letter,1)




