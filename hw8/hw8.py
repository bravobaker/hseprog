
# coding: utf-8

# In[ ]:


# 1 вариант
import random

def slova_dict():
    with open('slova.csv', encoding='utf-8') as f:
        d={}
        for line in f:
            line = line.replace('\n','').replace('\ufeff','')
            word, clue = line.split(';')
            if word in d:
                d[word].append(clue)
            else:
                d[word] = [clue]
    return d

   

def game():
    print ('Вам нужно угадать существительное.')
    print ('В качестве подсказки на экран выводится слово, которое часто употребляется в сочетании загаданным ')
    print ('Если Вы не сможете угадать слово с первой подсказки, Вам будет предложена еще одна. Всего подсказок будет столько, сколько букв в загаданном слове ')
    select_word = random.choice(list(slova_dict().keys()))
    select_clue = random.choice(slova_dict()[select_word])
    print ('Подсказка № 1',select_clue)
    att = len(select_word)
    print ('Количество оставшихся попыток: ', att) 
    users_w = input()
    for i in range(att-2):
        if users_w == select_word:
            print ('Ура! Верное слово!')
            break
        else:
            print ('Попробуйте другое слово. Количество оставшихся попыток: ', att - 1 - i)
            select_clue= random.choice(slova_dict()[select_word]) 
            print ('Подсказка №',i+2,':',select_clue )
        users_w = input()

    if users_w == select_word:
            print ('Ура! Верное слово!')
            new_game()
        
    else:
            print ('Попробуйте другое слово. Количество оставшихся попыток: 1 ')
            select_clue= random.choice(slova_dict()[select_word]) 
            print ('Подсказка №',i+3,':',select_clue )
            users_w = input()
            if users_w == select_word:
                print ('Ура! Верное слово!')
                new_game()
            else:
                print ('У вас кончились попытки:( Попробуйте снова.')
                new_game()
                


def new_game():
    print ('Если хотите попробовать еще раз, напишите "new game"')
    answer = input ()
    if answer == 'new game':
        game()

game()

