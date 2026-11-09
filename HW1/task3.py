countries = {
    "BY": "Belarus",
    "PL": "Poland",
    "DE": "Germany",
    "FR": "France",
    "ES": "Spain"
}

lst = list(countries.items())  # создаем список из списков (ключ, значение)
mylst=list()

for el in lst:  # заходим в каждый елемент списка, который тоже приводим к списку 
    ind = lst.index(el)
    el = list(el)
    el.reverse()
    mylst.insert(ind,tuple(el)) 
    
countries.clear() 
countries = dict(mylst)   
print(countries)
