
# coding: utf-8

# In[5]:


import os
def maxdepth():
    import os
    start = '.'
    herewego = start.count(os.sep)
    levelcount=[]
    for start, dirs, files in os.walk(start):
        level = start.count(os.sep)
        levelcount.append(level)
    print ('вот максимальная глубина папки в этом дереве:', max(levelcount))
    
maxdepth()

