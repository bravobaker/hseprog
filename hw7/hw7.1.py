
# coding: utf-8

# In[5]:


# coding: utf-8

# In[ ]:


def texttolist(): #эта функция открывает текст и делает из него список слов
    with open('Pride_and_Prejudice.txt', encoding = "utf-8") as f:
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



# In[19]:


def texttolist(name): #эта функция открывает текст и делает из него список слов
    with open(name, encoding = "utf-8") as f:
        text = f.read()
        for i in ['.',',','?','!',';',':','"','- ','-','—','(',')',"'",'”','’','*','&']:
            text = text.replace(i,'')
        text = text.lower()
        words = text.split()
        return words
    
texttolist(input("Введите название вашего файла:"))

    
def find_and_count_ings(name):#эта функция считает слова
    count = []
    b = 'ing'
    for word in texttolist(name):
        if word.endswith(b) == True:
            count.append(word)
    return len(count)
print ('слов на ing в этом тексте', find_and_count_ings())    

def search(name): #ищет введеное слово
    print ('введите слово на ing:')
    a = input()
    counter = []
    for word in texttolist(name):
        if word == a:
            counter.append(word)
    return len(counter)

print (search(),'- столько раз встречается введенное вами слово')




# In[28]:



def texttolist(name): #эта функция открывает текст и делает из него список слов
    with open(name, encoding = "utf-8") as f:
        text = f.read()
        for i in ['.',',','?','!',';',':','"','- ','-','—','(',')',"'",'”','’','*','&']:
            text = text.replace(i,'')
        text = text.lower()
        words = text.split()
        return words
 

def find_and_count_ings(name):#эта функция считает слова
    count = []
    b = 'ing'
    for word in texttolist(name):
        if word.endswith(b) == True:
            count.append(word)
    return len(count)
  

def search(name): #ищет введеное слово
    print ('введите слово на ing:')
    a = input()
    counter = []
    for word in texttolist(name):
        if word == a:
            counter.append(word)
    return len(counter)

def final(name):
    find_and_count_ings(name)
    print ('слов на ing в этом тексте', find_and_count_ings(name))
    print (search(name),'- столько раз встречается введенное вами слово')
    
    
final(input('Введите название файла: '))    
    
    


