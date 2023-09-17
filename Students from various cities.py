#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[19]:


student_data=readxl[readxl['Designation']=='Students']
channel_count=student_data['City'].value_counts()
freq=channel_count.head(10)


# In[20]:


plt.figure(figsize=(10, 6))
bars = plt.bar(freq.index, freq.values,color='skyblue')
freq.plot(kind='bar', color='skyblue')
plt.xlabel('Cities')
plt.ylabel('No of students')
plt.title('Students per city')
plt.xticks(rotation=45)

for i, value in enumerate(freq):
    plt.text(freq.index[i], value, f'{value}', ha='center', va='bottom')

plt.show()


# In[ ]:




