#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[3]:


df=pd.DataFrame(readxl)


# In[4]:


df['Family Income']=df['Family Income'].str.replace('[^\d.]','',regex=True)
df['Family Income']=pd.to_numeric(df['Family Income'],errors='coerce')
df['CGPA']=pd.to_numeric(df['CGPA'],errors='coerce')


# In[5]:


data=df.dropna(subset=['Family Income','CGPA'])


# In[8]:


cgpa_count=data['CGPA'].value_counts()
average_income_by_cgpa=data.groupby('Family Income')['CGPA'].mean()


# In[14]:


plt.scatter(df['Family Income'],df['CGPA'], color='b', label='Individual Data Points')
plt.plot(average_income_by_cgpa.index, average_income_by_cgpa.values, color='r', label='Average CGPA by Family Income')
plt.xlabel('Family Income')
plt.ylabel('CGPA')
plt.title('Relationship between CGPA and Family Income')
plt.legend()
plt.show()

