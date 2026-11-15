def characterPrinter():
    pozition = 0

    def inner(txt,n):
        nonlocal pozition
        for el in range(n):  # запускаем цикл от 0 до n
            print(txt[pozition],end="")  # выводим символы по индексу без разделителя 
            pozition = (pozition + 1) % len(txt) # рассчитывается индекс следующего символа с учетом длины строки
        print()
    return inner

printer = characterPrinter()

printer("Hello world!",3)
printer("Hello world!",4)
printer("Hello world!",4)
printer("Hello world!",2)