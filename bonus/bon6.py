
# coding: utf-8

# In[1]:


print('укажите  рост в см:')
h = float(input())
h = h/100
print('укажите  вес в кг:')
m = float(input())
i = round(m/(h*h),1)
print('индекс массы тела:', i)
if i <= 16:
    print ('выраженный дефицит массы тела')
elif 16 < i < 18.5:
    print ('недостаточная (дефицит) масса тела')
elif 18.5 <= i < 25:
    print ('норма')
elif 25 <= i < 30:
    print ('избыточная масса тела (предожирение)')
elif 30 <= i < 35:
    print ('ожирение первой степени')
elif 35 <= i < 40:
    print ('ожирение второй степени')
elif i >= 40:
    print ('ожирение третьей степени (морбидное)')

