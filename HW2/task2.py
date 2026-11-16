def join_strings(*args,sep = " "):
    res = ""
    res = sep.join(args)  # склеиваем все аргументы функции в строку с учетом разделителя

    return(print(res))

join_strings("Hellow","world")
join_strings("red","green","blue", sep = ", ")
join_strings("Python","is","awesame", sep = "-")
join_strings()