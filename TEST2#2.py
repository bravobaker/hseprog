
# coding: utf-8

# In[55]:


#задание 1
import re
def reading():
    with open('mystem.xml', encoding='utf-8') as f:
        file = f.read()
reading() 

def workplease(file):
    pls = re.sub(r'\n',' ', file)
    pls = re.search(r'<body>(.+?)</body>', pls)
    with open('sym.txt','w',encoding='utf-8') as f:
        f.write(str(len(pls.group(0))))
        
workplease(file)    
    


# In[12]:


import re #второе задание
import collections
def reading():
    with open('mystem.xml', encoding='utf-8') as f:
        file = f.read()
        
reading()
        
def workplease (file):
    morph = re.findall(r'gr="(.+?)"', file)
    d = collections.Counter(morph)
    with open('keys.txt','w',encoding='utf-8') as f:
        for key, value in list(reversed(sorted(d.items(), key=lambda item: item[1]))):
            f.write(str(key)+'\n')

workplease(file)


# In[53]:


import re
with open('mystem.xml', encoding='utf-8') as f:
    file = f.read()
    verbs = re.findall(r'gr="V(.+)?"', file)
    print(verbs)
    v_aspect = []
    for verb in verbs:
        if re.search(r'.+?,сов.+?', verb) is True:
            v_aspect.append(verb) #я знаю что он ничего не записывает, но так и не поняла почему
    #print (v_aspect)
    v_asp_sg = []
    for form in v_aspect:
        if re.search(r'.+?,ед.+?', form) is True:
            v_asp_sg.append(form)
    #print (v_asp_sg)
    with open('verbs.txt','w',encoding='utf-8') as f:
        f.write(str(len(v_asp_sg)))
        

    
    
    


# In[34]:




