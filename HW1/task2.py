text = """
Вчера Анна и Артем гуляли в парке. Анна заметила слово level на
старом плакате. Рядом кто-то написал radar, а чуть дальше было
нарисовано слово kayak. На скамейке сидел человек с книгой civic,
а возле фонтана дети мелом написали refer. Остальные слова в тексте
палиндромами не являются."""

text = text.lower()  
words = text.split()
words = [word.strip(" ,.?!+123457890()") for word in words]

for word in words:   # удаляем из списка слова с длиной меньше 2
    if len(word)<2:
        words.remove(word)

lst1 = {}
lst2 = {}
lst = []
for word in words:   
    lst1[word] = list(word)  # каждое слово рассматриваем как список символов
    lst2[word] = lst1[word][::-1]  # делаем второй список с перевернутым набором символов
    
    if lst1[word] == lst2[word]: # сравниваем два элемента как два списка из символов
       if word not in lst:
          lst.insert(words.index(word),word)
print(lst)
