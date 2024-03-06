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
Задача N2
"""
def insert_sort(table, column_ind):
	"""Sort dataset-like 2d array by selected column
	
	Arguments:
		table: dataset-like 2d array
		element_ind: index of column, by which sorting will be performed
	"""
	for i in range (1, len(table)):
		pos = i
		current = table[pos]
		while pos > 0 and current[column_ind] < table[pos - 1][column_ind]:
			table[pos] = table[pos - 1]
			pos -= 1
		table[pos] = current
	return table

#Заменим "None" на нули чтобы можно было сортировать, остальное в числа
for i in range(len(dataset)): 
    id, name, title, klass, score = dataset[i] 
    try:    	score = int(score)
    except:
    	score = 0 
    dataset[i] = [id, name, title, klass, score] 
    
#Отсортируем по оценкам (индекс столбца - 4), развернем чтобы было по убыванию

dataset = insert_sort(dataset, 4)[::-1]

# Заменим нули на "None" обратно, а числа конвертируем в строку

for i in range(len(dataset)): 
    id, name, title, klass, score = dataset[i] 
    if score == 0:
    	score = "None"
    else:
    	score = str(score)
    dataset[i] = [id, name, title, klass, score] 
    


# Создадим список со всеми десятиклассниками с максимальной оценкой
top_10k = []
for i in range(len(dataset)): 
    id, name, title, klass, score = dataset[i]
    if "10" in klass and score == "5":
    	top_10k.append(dataset[i])
	

#отсортируем по id по возрастанию

top_10k = insert_sort(top_10k, 0)

# выведем 3-х первых

print("Десятый класс")
for i in range(3):
	id, name, title, klass, score = top_10k[i]
	print(f"{i + 1} место: {name[1][0]}. {name[0]}")
	