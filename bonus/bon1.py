
# coding: utf-8

# In[2]:





# In[10]:


print('введите числа: ')
i=input()
num=0
sum=0
if i == '':
    print('числа не были введены')
else:
    i=int(i)
    max =i
    min=i   
    while i!='':
        i=int(i)
        num+=1
        sum+=i
        if i>max:
            max=i
        if i<min:
            min=i
        i=input()
    average=sum/num
    print('минимальное число: ', min)
    print('максимальное число: ', max)
    print('среднее арифметическое: ', average)

