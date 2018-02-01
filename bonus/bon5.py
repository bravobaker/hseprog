
# coding: utf-8

# In[ ]:


print ('Введите текст на английском:')
x = input()
for consonant in 'g','w','r','t','y','p','s','d','f','q','h','j','k','l','z','x','c','v','b','n','m':
    x = x.replace(consonant, consonant+'aig')
print('Aigy Paigy:',x)

