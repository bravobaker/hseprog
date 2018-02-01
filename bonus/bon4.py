
# coding: utf-8

# In[2]:


print ('введите слово/фразу:')
i = input()
for v in 'а','о','е','ю','я','э','у','и','ы','ё':
    i = i.replace(v,v +'с'+v)
print ('на кирпичном:', i)

