
filename = 'C:/Users/vovam/OneDrive/Рабочий стол/ПР10/Гусев Владимир Иванович_УБ-31_vvod.txt.txt'
with open(filename, 'r') as file:
    
    lines = file.readlines()


matrix = []
for line in lines:
    
    row = [int(num) for num in line.strip().split()]
    matrix.append(row)


for row in matrix:
    min_value = min(row)
    max_value = max(row)
    
    
    min_index = row.index(min_value)
    max_index = row.index(max_value)
    
    
    row[min_index], row[0] = row[0], row[min_index]
    
    
    row[max_index], row[-1] = row[-1], row[max_index]


output_filename = 'C:/Users/vovam/OneDrive/Рабочий стол/ПР10/Гусев Владимир Иванович_УБ-31_vivod.txt.txt'
with open(output_filename, 'w') as file:
    
    for row in matrix:
        file.write(' '.join(map(str, row)) + 'n')
