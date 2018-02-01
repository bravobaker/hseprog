
# coding: utf-8

# In[72]:


#вариант 1
import random

def kigo(): 
    #эта функция задает киго - "сезонное слово", которое было обязательным в эпоху классического хайку
    #киго косвенным образом указывает на время года, к которому относится картина, описываемая в стихотворении
    with open ('kigopls.txt', encoding='utf-8') as f:
        text = f.read()
    kigo = text.split(', ')
    return random.choice((kigo))

def sg_nouns():
    #
    with open('4_nouns.txt', encoding='utf-8') as f:
        sg_nouns = f.read()
    sg_nouns = sg_nouns.split(', ')
    return random.choice(sg_nouns)

def pl_nouns():
    with open('3_nouns.txt', encoding='utf-8') as f:
        pl_nouns = f.read()
    pl_nouns = pl_nouns.split(', ')
    return random.choice(pl_nouns)
def sg_adj():
    with open('sg_adj.txt', encoding='utf-8') as f:
        sg_adj = f.read()
    sg_adj = sg_adj.split(', ')
    return random.choice(sg_adj)

def pl_adj():
    with open('pl_adj.txt', encoding='utf-8') as f:
        pl_adj = f.read()
    pl_adj = pl_adj.split(', ')
    return random.choice(pl_adj)

def obj():
    #для переходного глагола
    with open('obj.txt', encoding='utf-8') as f:
        obj = f.read()
    obj = obj.split(', ')
    return random.choice(obj)

def adv():
    #для непереходного глагола
    with open('adv.txt', encoding='utf-8') as f:
        adv = f.read()
    adv = adv.split(', ')
    return random.choice(adv)

def verb_intr_pl():
    with open('verb_intr_pl.txt', encoding='utf-8') as f:
        verb_intr_pl = f.read()
    verb_intr_pl = verb_intr_pl.split(', ')
    return random.choice(verb_intr_pl)

def verb_intr_sg():
    with open('verb_intr_sg.txt', encoding='utf-8') as f:
        verb_intr_sg = f.read()
    verb_intr_sg = verb_intr_sg.split(', ')
    return random.choice(verb_intr_sg)

def verb_tran_sg():
    with open('verb_tran_sg.txt', encoding='utf-8') as f:
        verb_tran_sg = f.read()
    verb_tran_sg =  verb_tran_sg.split(', ')
    return random.choice(verb_tran_sg)

def verb_tran_pl():
    with open('verb_tran_pl.txt', encoding='utf-8') as f:
        verb_tran_pl = f.read()
    verb_tran_pl = verb_tran_pl.split(', ')
    return random.choice(verb_tran_pl)

def verb_choice_sg():
    #эта функция собирает вариант третей строки из глагола в единственном числе и прямого дополнения/сирконстанта
    choice = random.randint(1,2)
    if choice == 1:
        return (verb_tran_sg()) + ' ' + (obj())+ random.choice(punc)
    elif choice == 2:
        return (verb_intr_sg()) + ' ' + (adv()) + random.choice(punc)

def verb_choice_pl():
    #эта функция собирает вариант третей строки из глагола во множественном числе и прямого дополнения/сирконстанта
    choice = random.randint(1,2)
    if choice == 1:
        return (verb_tran_pl()) + ' ' + (obj())  + random.choice(punc)
    elif choice == 2:
        return (verb_intr_pl()) + ' ' + (adv())+ random.choice(punc)
    
    
    
pu = [".",",","!","?"," -","..."]#это набор знаков препинания для первой строки
punc = [".","!","?","..."]#это набор знаков препинания без запятой и тире для второй строки, т.к. должен быть маркирован конец предложеня
#кажется предложения в русской традиции перевода хайку не обязательно должны начинаться с заглавной буквы, никакого правила не нашлось
#я сделала с маленькой, потому что так красивее

def haiku():
    #эта функция собирает стих в зависимости от рода существительного во второй строке
    comb = random.randint(1,2) 
    if comb == 1:
        haiku1 = (kigo()) + random.choice(pu) + '|' + (sg_nouns()) + ' ' + (sg_adj()) + '|' +(verb_choice_sg())
        haiku1 = haiku1.split('|')
        haiku1 = '\n'.join(haiku1)
        return haiku1
        
        
    elif comb == 2:
        haiku2 = (kigo())+ random.choice(pu) + '|' + (pl_nouns()) + ' ' + (pl_adj()) + '|' + (verb_choice_pl())
        haiku2 = haiku2.split('|')
        haiku2 = '\n'.join(haiku2)
        return haiku2
         
print(haiku()) 

