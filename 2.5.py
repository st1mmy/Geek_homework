number = int(input("Enter number: "))
list = [7, 4, 3, 2]
c = list.count(number)
for element in list:
    if c > 0:
        i = list.index(number)
        list.insert(i+c, number)
        break
    else:
        if number > element:
            j = list.index(element)
            list.insert(j, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)