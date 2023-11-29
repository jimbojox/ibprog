# Открываем файл для чтения
filename = 'C:/Users/vovam/OneDrive/Рабочий стол/ПР10/Гусев Владимир Иванович_УБ-31_vvod.txt.txt'
with open(filename, 'r') as file:
    # Читаем данные из файла
    lines = file.readlines()

# Обрабатываем данные
matrix = []
for line in lines:
    # Разбиваем каждую строку на элементы списка и преобразуем их в целые числа
    row = [int(num) for num in line.strip().split()]
    matrix.append(row)

# Вычисляем минимальные и максимальные элементы в каждой строке матрицы
for row in matrix:
    min_value = min(row)
    max_value = max(row)
    
    # Ищем индексы минимального и максимального элемента
    min_index = row.index(min_value)
    max_index = row.index(max_value)
    
    # Меняем минимальный элемент и первый элемент
    row[min_index], row[0] = row[0], row[min_index]
    
    # Меняем максимальный элемент и последний элемент
    row[max_index], row[-1] = row[-1], row[max_index]

# Открываем файл для записи
output_filename = 'C:/Users/vovam/OneDrive/Рабочий стол/ПР10/Гусев Владимир Иванович_УБ-31_vivod.txt.txt'
with open(output_filename, 'w') as file:
    # Записываем результаты в файл
    for row in matrix:
        file.write(' '.join(map(str, row)) + 'n')
