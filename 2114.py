sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_length = 0
for group1 in sentences:
    group1_s = group1.split(" ")
    if len(group1_s) > max_length:
      max_length = len(group1_s)

print(max_length)