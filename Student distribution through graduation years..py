#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[4]:


df=pd.DataFrame(readxl)


# In[5]:


student=df[df['Designation'].str.strip().str.lower().str.contains('student')].copy()
graduation= student['Year of Graduation']


# In[8]:


plt.hist(graduation, bins=10, edgecolor='red', alpha=0.7)
plt.xlabel("Year of Graduation")
plt.ylabel("Number of Students")    
plt.xticks(range(int(min(graduation)), int(max(graduation)) + 1))    
for i in range(int(min(graduation)), int(max(graduation)) + 1):
    count = len(graduation[graduation== i])
    plt.text(i, count + 1, str(count), ha='center', va='bottom')
plt.show()


# In[ ]:




