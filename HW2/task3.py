def reduce(a,b,*args,action):
    
    rez = action(a,b)  # первое действие с первыми двумя аргументами

    for el in args:  # последующие действия с первым результатом и следующими аргументами
        rez = action(rez,el)

    return(rez)


summa = reduce(1, 2, 3, action = lambda x, y: x + y)
print(summa)
minimum = reduce(1, 2, 3, 0, action = lambda x, y: x if x < y else y)
print(minimum)
product = reduce(2, 3, 4, action = lambda x, y: x * y)
print(product)