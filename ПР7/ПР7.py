#Вариант 1.1

def square(figure):

    if figure == 'Квадрат':
        a = int(input('Введите длину: '))
        print('Площадь квадрата:',a**2)

    elif figure == 'Прямоугольник':
        a = int(input('Введите длину: '))
        b = int(input('Введите ширину: '))
        print('Площадь прямоугольника:', (a+b)*2)

    elif figure == 'Круг':
        a = int(input('Введите радиус: '))
        print('Площадь круга:', 3.14 * (a**2))

    elif figure == 'Ромб':
        a = int(input('Введите длину первой диагонали: '))
        b = int(input('Введите длину второй диагонали: '))
        print('Площадь ромба:',(a+b)/2)

square(str(input('Введите название фигуры: ')))

#Вариант 1.2

m = [randint(1,100) for i in range(15)]
n = [randint(1,100) for i in range(10)]
c = [randint(1,100) for i in range(5)]

cr_m = 0
cr_n = 0
cr_c = 0

for i in m:
    cr_m += i
print('Сумма элементов первого массива равна:',cr_m)
cr_m /= len(m)
print('Среднее арифметическое первого массива равно:',cr_m,'\n')

for i in n:
    cr_n += i
print('Сумма элементов второго массива равна:',cr_n)
cr_n /= len(n)
print('Среднее арифметическое второго массива равно:',cr_n,'\n')

for i in c:
    cr_c += i
print('Сумма элементов третьего массива равна:',cr_c)
cr_c /= len(c)
print('Среднее арифметическое третьего массива равно:',cr_c,'\n')
# Вариант 3.1

def hypotenuse(a,b):
    return sqrt(a**2 + b**2)

if hypotenuse(5,10) > hypotenuse(10,15):
    print('Первая гипотенуза больше')
else:
    print('Первая гипотенуза меньше')

# Вариант 3.2

s = ['t','z','b','u','a']

s.sort()
print(s)
