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


student=df[df['Designation'].str.strip().str.lower().str.contains('student')].copy()
student.dropna(inplace=True)


# In[5]:


print(student['City'].unique())


# In[13]:


student['CGPA']=pd.to_numeric(student['CGPA'], errors='coerce')
cgpa_by_city = student.groupby('City')['CGPA'].mean().reset_index()
cgpa_by_city= cgpa_by_city.sort_values(by='CGPA', ascending=False)
cgpa_by_city=cgpa_by_city.head(20)


# In[14]:


plt.figure(figsize=(10, 6))
plt.bar(cgpa_by_city['City'], cgpa_by_city['CGPA'], color='blue')
plt.xlabel('City', fontsize=12)
plt.ylabel('Average GPA', fontsize=12)
plt.title('Average GPA of Students in Top 10 Cities', fontsize=14)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

for i, value in enumerate(cgpa_by_city['CGPA']):
    plt.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom')

plt.show()


# In[ ]:




