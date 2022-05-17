s = "Let's take LeetCode contest"
new_s = s.split(" ")
result_s = ""

for group1 in new_s:
    # to_be_added = "".join(reversed(group1))
    to_be_added = group1[::-1]
    result_s = result_s + to_be_added + " "
result_s = result_s.rstrip()
print(result_s)

