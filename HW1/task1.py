#numbers = [15,7,2,0,21]
numbers = [4,6,2,11,1,11,5]

max = numbers[0]    #находим максимальный по значению элемент списка
for el in numbers:
    if el > max:
        max = el

res = [el for el in numbers if el != max]   #новый список без максимального элемента

max2 = res[0]    #находим максимальный по значению элемент нового списка
for el in res:
    if el > max2:
        max2 = el
print(max2)    #выводим второй максимальный элемент
