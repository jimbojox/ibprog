#Вариант 1.1

N = 3

A = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

c = 0
s = 0
for i in range(N):
	for j in range(i + 1, N):
		if A[i][j] > 0:
			s += A[i][j]
			c += 1

print("Число:",c)
print("Сумма:",s)

#Вариант 1.2

N = 3
M = 4

A = [
[12,11,9,10],
[8, 7, 6, 5],
[4, 3, 2, 1]]

for i in range(N):
	i_min = 0
	v_min = A[i][0]
	for j in range(M):
		if A[i][j] < v_min:
			i_min = j
			v_min = A[i][j]
	c = A[i][0]
	A[i][0] = A[i][i_min]
	A[i][i_min] = c

for i in range(N):
	i_max = 0
	v_max = A[i][0]
	for j in range(M):
		if A[i][j] > v_max:
			i_max = j
			v_max = A[i][j]
	c = A[i][M-1]
	A[i][M-1] = A[i][i_max]
	A[i][i_max] = c

for i in range(N):
	for j in range(M):
		print("%2d " % A[i][j], end='')
	print()

# Вариант 3.1

a = list()
n = 3

for i in range(n):
    b = list()
    for j in range(n):
        b.append(2)
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

