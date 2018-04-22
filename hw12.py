
# coding: utf-8

# In[8]:


import re
import os
def formeplease():
    lst = []
    for name in os.listdir('.'):
        if re.search(r'[0-9]', name):
            if os.path.isdir(name):
                lst.append(name)
    return(lst)
    
    
def dontbedead(lst):
    if len(lst) == 0:
        print ("Нет папок, содержащих в названии цифры")
    else: 
        print(len(lst),"- столько папок содержат цифры в названиях")
        print ("Названия этих папок:")
        print('\n'.join(lst))
        
dontbedead(formeplease())

