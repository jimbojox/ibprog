# задание 7
a = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, a + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)
# задание 8
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
# задание 1
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)
# задание 4
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)
# задание 5
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(sum)
