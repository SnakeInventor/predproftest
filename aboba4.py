import random

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
Задача 4
"""

"""
Реализуйте методы/функции, которые будут генерировать логины и пароли для пользователей.
"""

"""
Пароль должен состоять из 8 символов, включать в себя заглавные, строчные буквы английского алфавита и цифры.
"""

def make_password():
    """Makes random 8 symbol password from english alphabet and numbers"""

    # все символы, которые могут быть в пароле (строчные и заглавные английские буквы, цифры)
    smol_letters = "qwertyuiopasdfghjklzxcvbnm"
    BIG_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    digits = "0123456789"

    bukvi = smol_letters + BIG_letters + digits
    
    # восемь раз выбираем случайный символ из доступных
    parol = [random.choice(bukvi) for c in range(8)]
    
    parol = "".join(parol)
    return parol


"""
Логин должен состоять из фамилии и инициалов, например,
если школьника зовут Соколов Иван Иванович,
его логин должен выглядеть как Соколов_ИИ.
"""

# Функция, делающая логин из Фамилии, первой буквы имени и первой буквы отчества
def make_login(FIO):
    """ Makes login for user, abbreviating first name and patronymic

    Arguments:
    FIO: array containing last name, first name and patronymic
    """
    return FIO[0] + "_" + FIO[1][0] + FIO[2][0]


for i in range(len(dataset)):
    id, name, title, klass, score = dataset[i]

    login = make_login(name)
    password = make_password()

    # добавляем два новых столбца в строку
    dataset[i] = [id, name, title, klass, score, login, password] 

"""
Последним этапом полученный список записать в новый students_password.csv файл.
"""

#(!!!НЕ ЗАБЫВАЕМ УКАЗАТЬ НОВЫЕ СТОЛБЦЫ ПРИ ФОРМАТИРОВАНИИ!!!)
### ЗАПИСЬ ДАННЫХ В ФАЙЛ

# Делаем так чтобы каждая ячейки в списке содержала только одну строку 

 #(!!!НЕ ЗАБЫВАЕМ ДОБАВИТЬ НОВЫЕ СТОЛБЦЫ ПРИ ФОРМАТИРОВАНИИ!!!)   
for i in range(len(dataset)):
    id, name, title, klass, score, login, password = dataset[i]
    
    id = str(id)
    name = " ".join(name)
    dataset[i] = [id, name, title, klass, score,  login, password]

# добавляем названия столбцов к сериализованным данным
serialized_dataset = header + to_csv_string(dataset)

# "w+" - режим записи, плюс означает, что файл создастся если не существует.
# encoding="utf8" - кодировка для .csv формата


with open("students_password.csv","w+", encoding="utf8") as F:
    F.write(serialized_dataset) # записывает строку с сериализованными данными в НОВЫЙ файл