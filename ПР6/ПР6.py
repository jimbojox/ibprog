# Вариант 5.1
m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

for i in range(len(m)-1):
    if (m[i] < 0) and (m[i+1] < 0):
        print('Пара отрицательных чисел:',m[i],m[i+1])

# Вариант 5.2
m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

n = list()

for i in range(len(m)):
    if n.count(m[i]) < 1:
        n.append(m[i])

print('Полчуенный моссив:',n,'\n',m)

# Вариант 3.1
d = list()
n = int(input('Введите длину массива: '))
symm = 0

for i in range(n):
    print('Введите',i+1,'элемент массива')
    d.append(int(input()))

for i in range(n):
    if i % 2 == 1:
        symm += d[i]

print('Полученный массив:',d,'\n','Сумма элементов с нечетным индексом:',symm)

# Вариант 3.2
m = list()

for i in range(8):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

for i in range(len(m)):
    if m[i] < 15:
        m[i] **= 2
print('Полученный массив:',m)
