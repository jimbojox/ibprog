import requests
import json
from tkinter import *

def get_repo_info():
    repo_name = entry.get() 
    
   
    response = requests.get(f'https://api.github.com/{repo_name}')
    if response.status_code == 200: # Если запрос успешный
        repo_info = response.json()
        
       
        with open('site', 'w') as file:
            file.write(f"'company': {repo_info['owner']['company']},n")
            file.write(f"'created_at': {repo_info['created_at']},n")
            file.write(f"'email': {repo_info['owner']['email']},n")
            file.write(f"'id': {repo_info['id']},n")
            file.write(f"'name': {repo_info['name']},n")
            file.write(f"'url': {repo_info['url']}n")
    else:
        print("Ошибка при выполнении запроса")

win = Tk()
win.configure(background='azure3')
win.title('Информация о репозитории')
win.geometry('500x400+500+100')

title = Label(win,text='Введите название репозитория',width=30,height=1,font=('Arial 20 bold'),bg='azure3').grid(row=0)
bar_text_vvod = Entry(win,width=35,borderwidth=5)
bar_text_vvod.grid(row=1)
bar_text_vvod.focus()
button = Button(win,text='Получить информацию',width=30,height=2,command=lambda :using_button()).grid(row=2,pady=20)


win.mainloop()
