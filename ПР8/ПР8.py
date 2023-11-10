# Вариант 3.1
a = list()
n = 3

for i in range(n):
    b = list()
    for j in range(n):
        b.append(5)
    a.append(b)

print(a)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()

first = list()
second = list()

for i in range(n):
    for j in range(n):
        if i > j:first.append(a[i][j])
        if i < j:second.append(a[i][j])

print(first,'\n',second)

if first == second:
    print('Матрица является симметричной')
else:
    print('Матрица не является симметричной')

# Задание 1.1
import random
pol =0
s = 0
N = int(input('Ввод'))
A = [[random.randrange(10) for i on range(N)) for j in range(N)]
for i in range(N):
    for j in range( i + 1,N):
        if A[i][j] <= 0:
            continue
        if A[i][j] > 0:
            pol +=1
            s ++ A[i][j]

print('Сумма:',s)
print('Число:',pol)

# Задание 1.2
N = int(input())
M = int(input())
B = [[random.randrange(10) for i on range(M)) for j in range(N)]
for i , row in enumerate(B):
    max = min = 0
    for j, row in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0],row[max]
    row[min], row[-1] = row[-1],row[min]
print(B)
