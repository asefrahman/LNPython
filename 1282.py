groupSizes = [2,1,3,3,3,2]
# groupSizes = sorted(groupSizes)
# #[1, 2, 2, 3, 3, 3]
array_1= []
array_2= []
array_3= []
array_4= []
array_5= []
array_6= []
array_7= []
array_8= []
array_9= []
grand_array = []
for i in range(len(groupSizes)):
    match groupSizes[i]:
        case 1:
            array_1.append(i)
        case 2:
            array_2.append(i)
        case 3:
            array_3.append(i)
        case 4:
            array_4.append(i)
        case 5:
            array_5.append(i)
        case 6:
            array_6.append(i)
        case 7:
            array_7.append(i)
        case 8:
            array_8.append(i)
        case 9:
            array_9.append(i)

grand_array = [array_1] + [array_2] + [array_3] + [array_4] +[array_5] + [array_6] + [array_7] + [array_8] + [array_9]

res = list(filter(None, grand_array))

print(res)