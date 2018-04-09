
# coding: utf-8

# In[19]:


import re

def species():    
    with open ('komar.htm', encoding='utf-8') as f:
        html = f.read()
    return html
        

def magic(html):
    new_species = re.sub(r'(\W)комар(а(?:ми?|х)?|у|е|ы|о(?:в|м|)|)(\W)', r'\1слон\2\3', html)
    new_species = re.sub(r'(\W)Комар(а(?:ми?|х)?|у|е|ы|о(?:в|м|)|)(\W)', r'\1Слон\2\3', new_species)
    with open('zamena.htm', 'w', encoding='utf-8') as f:
        f.write(new_species)
        

magic(species())#в части про болезни есть слово "слоновость", это не "комаровость" заменилась, это болезнь такая, она там сразу была

