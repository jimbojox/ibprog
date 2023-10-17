# 6 Задание
s = "aasaaaahhwhaa"
count = len(s) - len(s.replace("a", ""))
print(s)
print(str(count))

# 10 Задание
s = "My name is vladimir"
print(s.title())

# 14 Задание
s = "Я Владимир и я безумно увлекаюсь рыбалкой"
for l in s.split():
    if(l.startswith("а") or l.endswith("я")):
       print(l)
       
# 5 Задание
s = "My Name Is Vladimir"
print(s.lower())

# 2 Задание
s = "::::;№;:".split(":")
print("%".join(s))
print(len(s)-1)

# 1 Задание
s = "ель елка шар земля".lower().count('е')
print('Кол-во слов начинающиеся на е'.count('е'))

# 15 Задание
s = "ттттттттууфуфуфуффутт"
print('Кол-во символов т в строке равно',s.count('т'))

# 8 Задание
s = "My Name Is Vladimir"
words = s.split()
num_words = len(words)
print("Кол-во слов:",num_words)

# 12 Задание
s =" Змея семья шар карта"
for w in s.split():
	if(w.endswith("я")):
		print(w)
