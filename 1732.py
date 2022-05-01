gain = [-5, 1, 5, 0, -7]
#altitude = [0, -5, -4, 1, 1, -6]
alt= [0]
# highest = 0
# i = 0
# alt[1]= 0 + gain[0]
# for start in range(2,len(gain)):
#     if gain [0] or gain [1]:
#         continue
#     else:
#         alt.append(start+)
#     for start2 in range(start+1, len(gain)+1):
#     if i == 0:
#         value = 0 - start
#         alt.append(value)
#         i += 1
#     else:
i = 1
for start in gain:
    if i <= len(gain):
        alt[i] = alt[i-1]+ start
        i +=1
print(alt)


