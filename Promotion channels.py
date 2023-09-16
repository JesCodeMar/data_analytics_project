#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[16]:


student_data=readxl[readxl['Designation']=='Students']
channel_count=student_data['Promotion Channels'].value_counts()
freq=channel_count.head()
freq


# In[24]:


plt.figure(figsize=(10, 6))
bars = plt.bar(freq.index, freq.values,color='skyblue')
freq.plot(kind='bar', color='skyblue')
plt.xlabel('Promotion Channel')
plt.ylabel('Student Count')
plt.title('Promotion Channel Usage Frequency')
plt.xticks(rotation=45)

for i, value in enumerate(freq):
    plt.text(freq.index[i], value, f'{value}', ha='center', va='bottom')

plt.show()


# In[ ]:




