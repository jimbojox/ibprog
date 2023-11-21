#Блок А Задание 3

a = int(input("Введите число: ")) 
revr_a = 0     
def recur_reverse(a): 
    global revr_a   
    if (a > 0): 
        Reminder = a % 10 
        revr_a = (revr_a * 10) + Reminder 
        recur_reverse(a // 10) 
    return revr_a 

revr_a = recur_reverse(a) 
print("n Перевернутое число = %d" % revr_a) 

#Блок Б задание 3

def f():
    n = int(input('Введите длину строки: '))
    for i in range(n):
        b = int(input('Введите число: '))
        if (i+1) % 2 != 0:
            print(b)
        if b == 0:
            break

f()
