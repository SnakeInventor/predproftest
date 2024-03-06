### УНИВЕРСАЛЬНЫЕ ФУНКЦИИ

def format_data(data):
    """ Loads serialized .csv into dataset-like 2d array 
    
    Arguments:
    data: the string with .csv data
    """
    table = [] 
    data = data.split("\n") #  "\n" - это перенос строки

    for row in data:
        row = row.split(",") # ВАЖНО!!!! Нужно вписать в split ЗАПЯТУЮ, иначе все поломается
        if len(row) == 5: # Если длина соответствует, форматируем строку и добавляем в таблицу
            id, name, title, klass, score = row # создаем переменные для каждой ячейки в строке
            id = int(id) # конвертируем id в число, чтобы потом было удобнее
            name = name.split() # Разбиваем ФИО на список из 3 слов
            title = title
            klass = klass
            score = score # в score встречаются не только числа, но и "None", поэтому в число не сконвертируешь

            table.append([id, name, title, klass, score]) # добавляем в новый массив строку

    return table

def to_csv_string(data):
    """ Serializes dataset-like 2d array into .csv format  
    
    Arguments:
    data: dataset-like 2d array
    """
    s = ""
    for row in data:
        s += ",".join(row) + "\n" # объединяет ячейки в строку, разделенную запятыми и в конце добавляет перенос на следующую строку
    return s




### ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА

# "r" - режим чтения
# encoding="utf8" - указываем режим кодировки utf8, это важно, т.к. иначе .csv файл не прочитается

with open("students.csv", "r" , encoding="utf8") as F:
    header = F.readline() # читает первую строку
    raw_data = F.read() # читает все остальное

# dataset - эдакая табличка с нашими данными, с которой мы будем работать, она представляет из себя двумерный массив
dataset = format_data(raw_data)


"""
Задание 5
"""

"""
Если используются прописные и строчные буквы 
русского алфавита, а также символ пробел, то возможет выбор p = 67

Хорошим выбором для  m является 
какое-либо большое простое число. (можно использовать m = 10**9
+9, это большое число, но все же 
достаточно малое, чтобы можно было выполнять умножение двух значений, используя 64-битные 
целые числа)
"""

def my_hash(s):
    """Creates hash sum for given string

    Arguments:
    s: string made from kirrilick letters and spaces
    """

    
    # символы встречающиеся в ФИО для хеширования !очень важно! добавить в конце пробел
    d = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
    # превращаем символ в его номер в сторке d
    s = [d.index(c) + 1 for c in s]
    p = 67
    m = 10**9 + 9
    
    h = 0
    for i in range(len(s)):
        h += (s[i]*(p**i % m)) % m
    return h % m

"""
Необходимо составить хэш-таблицу, в 
которой будет выстроено соответствие ФИО и значения хэша ФИО. На основании этого 
необходимо составить хэш-таблицу и заменить id ученика на полученный хэш
"""
for i in range(len(dataset)):
    id, name, title, klass, score = dataset[i]
    
    
    id = my_hash(" ".join(name))
    dataset[i] = [id, name, title, klass, score]



"""
Результаты необходимо записать в новый 
students_with_hash.csv файл.
"""


### ЗАПИСЬ ДАННЫХ В ФАЙЛ

# Делаем так чтобы каждая ячейки в списке содержала только одну строку
for i in range(len(dataset)):
    id, name, title, klass, score = dataset[i]
    
    id = str(id)
    name = " ".join(name)
    dataset[i] = [id, name, title, klass, score]

# добавляем названия столбцов к сериализованным данным
serialized_dataset = header + to_csv_string(dataset)

# "w+" - режим записи, плюс означает, что файл создастся если не существует.
# encoding="utf8" - кодировка для .csv формата


with open("students_with_hash.csv","w+", encoding="utf8") as F:
    F.write(serialized_dataset) # записывает строку с сериализованными данными в НОВЫЙ файл
