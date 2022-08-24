list = []
for number in range(1500,2701):
    if (number % 7 ==0) and (number % 5 ==0):
        list.append(str(number))

print(','.join(list))
