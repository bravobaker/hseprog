
# coding: utf-8

# In[ ]:


def texttolist(): #эта функция открывает текст и делает из него список слов
    with open(name, encoding = "utf-8") as f:
        text = f.read()
        for i in ['.',',','?','!',';',':','"','- ','-','—','(',')',"'",'”','’','*','&']:
            text = text.replace(i,'')
        text = text.lower()
        words = text.split()
        return words
    
def find_and_count_ings():#эта функция считает слова
    count = []
    b = 'ing'
    for word in texttolist():
        if word.endswith(b) == True:
            count.append(word)
    return len(count)
print ('слов на ing в этом тексте', find_and_count_ings())    

def search(): #ищет введеное слово
    print ('введите слово на ing:')
    a = input()
    counter = []
    for word in texttolist():
        if word == a:
            counter.append(word)
    return len(counter)

print (search(),'- столько раз встречается введенное вами слово')


# In[4]:




