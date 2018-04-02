
# coding: utf-8

# In[ ]:



import re

def htmltotext():
    html=''
    try:
        name = input('Введите имя файла: ')
        with open(name, encoding = "utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print('Такого файла не существует или вы ничего не ввели')
    return html
    
def search():
    try:
        html = htmltotext()
        m = re.search(r'title="Столица">Столица<\/a><\/b>\n.+\n.+title="(.+?)[ "]', html)
        with open ('capital.txt', "a", encoding="utf-8") as f:
            f.write(m.groups()[0]+'\n')
    except AttributeError:
        print ('Столицу найти не удалось :(')
search()

