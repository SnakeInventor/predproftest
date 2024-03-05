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
ЗАДАЧА НОМЕР 1
"""

# =  Первая треть задания =
"""
Пожалуйста, подскажите Владимиру какую оценку он получил. Формат вывода: Ты получил: <ОЦЕНКА>, за проект - <id> 
"""
# Ищем такую строку, где в ФИО будет и "Хадаров" и "Владимир" одновременно
# Затем выводим оценку и название проекта из этой же строки
for i in range(len(dataset)): 
    id, name, title, klass, score = dataset[i]
    if 'Хадаров' in name and 'Владимир' in name:
        print(f"Ты получил: {score}, за проект-{title}") 
        break


# = Вторая треть задания =
"""
Поставьте вместо ошибки среднее значение по классу и округлите до трех знаков после запятой.
"""
# Создаем массив, в который будем записывать имеющиеся оценки
ocenki = []

# Проходимся по всей таблице, пробуем преобразовать оценку в число и добавить в массив
# Если не получается - не делаем ничего 
# (туда можно любой литерал засунуть вместо нуля: число, пустой список и т.д, главное чтобы строчка после except пустой не была)

for i in range(len(dataset)):
    id, name, title, klass, score = dataset[i]
    try:
        ocenki.append(int(score))
    except:
        0 # не делать ничего 

# считаем среднее арифметическое из всех оценок, округляем до 3 знаков после запятой
average_score = round(sum(ocenki)/len(ocenki), 3)

# Если стоит "None" вместо оценки, записываем туда среднее арифметическое
for i in range(len(dataset)):
    id, name, title, klass, score = dataset[i]
    
    if score == "None":
        score = str(average_score)

    dataset[i] = [id, name, title, klass, score]


# = Последняя треть задания =
"""
Сохраните данные в новую таблицу с названием student_new.csv. 
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


with open("students_new.csv","w+", encoding="utf8") as F:
    F.write(serialized_dataset) # записывает строку с сериализованными данными в НОВЫЙ файл