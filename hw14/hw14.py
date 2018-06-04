
# coding: utf-8

# In[1]:


import re
import nltk.data

def stopsmiling():
    tokenizer = nltk.data.load('nltk_data/tokenizers/punkt/english.pickle')
    f = open("test1.txt")
    a = f.read()
    b = tokenizer.tokenize(a)
    c = []
    for sentence in b:
        s = sentence.lower()
        s = ' '.join(re.findall(r'[a-z0-9]+', s))
        c.append(s)
    return c
        
c = stopsmiling()


def itsnotokay():
    data = []
    for sentence in c:
        s = sentence.split()
        data1 = [word.lower() for word in s if len(word)>7]
        data.extend(data1)
    return data

data = itsnotokay()

def itiswhatitis():
    dictionary = {word: len(word) for word in data}
    for key, value in dictionary.items(): 
        print('{:-<20}'.format(key),'{:>2}'.format(value))
    
itiswhatitis()

