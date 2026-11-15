def get_day_type(num_day):
    if not isinstance(num_day,int):
       return (print(None))

    if num_day <0 or num_day>365:
        return (print(None))
    
    dc = {x: (x+3) % 7 for x in range(1,366)}  # генерируем словарь из пары номер дня : номер дня недели
    dc |= {y:5 for y in (1,2,7,121,129,131,184,311,359)} # обновляем словарь значениями выходного дня для праздников

    if dc[num_day] in (5,6):
        return(print("day off"))
    else:
        return(print("workday"))

get_day_type(1)
get_day_type(5)
get_day_type(400)