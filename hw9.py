
# coding: utf-8

# In[3]:


import re

def doctotext():
    name = input('Введите имя файла: ')
    with open(name, encoding = "utf-8") as f:
        text = f.read()
        text = text.lower()
        text = ' '.join(re.findall(r'[а-я]*', text))
        return text
    

def search(text):
    look = re.compile(r'(откро(?:й(те)?|ю[т]?|е(?:м|шь|те|т))|откры(?: т |т(?:ь|ы(?:й|ми?|х|е)?|о(?:го|му?|й|ю|е)?|ая?|ую?)?|вш(?:и(?:ми|[йехм])?|ая|е(?:го|му|м|й|ю|е)|ую)|в |л[аои]?))(ся|сь)?(?= )')
    return re.findall(look, text)
    
    
def printit():
    words = []
    for word in search(doctotext()):
            word1 = ''.join(word)
            words.append(word1)
    if words != []:
        print(words)
    else:
        print ('Форм этого слова в тексте не нашлось :с')
    
    
printit()

