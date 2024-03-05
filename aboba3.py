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
ЗАДАЧА НОМЕР 3
"""

"""
На вход будет получать id проекта (гарантируется, что вводимые числа всегда целые)

На выходе будет предоставлять информацию о ученике, который делал
этот проект и его оценку за этот проект в формате:

Проект № <N> делал: <И. Фамилия> он(а) получил(а) оценку - <ОЦЕНКА>.

Если по заданному запросу ничего не найдено вывести: Ничего не найдено
"""


# В задании сказано пройтись по массиву с помощью линейного поиска (без встроенных функций),
# поэтому напишем свою функцию для этого
def find_index_of_project_by_id(table, t_id):
    """Returns index of the row which has specified project id
    
    Arguments:
    table: dataset-like 2d array
    t_id: project id that we want to find
    """

    for i in range(len(table)):
        if table[i][0] == t_id:
            return i

ids = [int(row[0]) for row in dataset] # создает список всех id проектов

# смотрим что введет юзер
usr_input = input()
while(usr_input != "СТОП"): # Если пользователь ввел "СТОП" - бесконечный цикл останавливается (программа завершится)

    # Пытается преобразовать ввод в число, если не получается, ругается в коноль
    try:
        target_id = int(usr_input)
    except:
        print('Неккоректный ввод! Напишите ID проекта в виде числа или команду "СТОП" для остановки программы')
        

    # Проверяет чтобы id вообще был в списке, иначе ругается в консоль
    if (target_id not in ids):
        print(f"Ничего не найдено.")
    else:
        # используем свою функцию поиска
        row_index = find_index_of_project_by_id(dataset, target_id)

        id, name, title, klass, score = dataset[row_index]

        print(f"Проект № {id} делал: {name[1][0]}. {name[0]} он(а) получил(а) оценку - {score}")

    target_id = -1 # Обнуляем id
    usr_input = input() # В конце ждем ввода пользователем новых указаний