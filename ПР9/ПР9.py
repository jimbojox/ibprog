#Блок А Задание 3

num = int(input("Введите число: ")) 
revr_num = 0     
def recur_reverse(num): 
    global revr_num   
    if (num > 0): 
        Reminder = num % 10 
        revr_num = (revr_num * 10) + Reminder 
        recur_reverse(num // 10) 
    return revr_num 

revr_num = recur_reverse(num) 
print("n Перевернутое число = %d" % revr_num) 

#Блок Б Задание 3

def f():
    a = int(input('Введите число: '))
    if a == 0:
        exit()
    else:
        print(a)
        f_1()

def f_1():
    a = int(input('Введите число: '))
    if a == 0:
        exit()
    else:f()
f()
