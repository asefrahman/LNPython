word1 = "abcd"
word2 = "pq"

result = ""
index = 0
while (index < len(word1) and index < len(word2)):
    result = result + word1[index]
    result = result + word2[index]
    index += 1

if len(word1) > len(word2):
    result = result + word1[index:len(word1)]

if len(word2) > len(word1):
    result = result + word2[index:len(word2)]


print(result)
