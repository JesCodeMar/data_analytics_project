#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[3]:


student_data=readxl[readxl['Designation']=='Students']


# In[4]:


student_data['Events'].unique()


# In[18]:


data_science_keywords=['Data Science','Artificial Intelligence','ML','Machine Learning','Deep Learning','Data Visualization','Data Analysis']


# In[19]:


data_science_events = student_data[student_data['Events'].str.contains('|'.join(data_science_keywords), case=False)]


# In[20]:


event_count=data_science_events['Events'].value_counts()
freq=event_count
freq


# In[22]:


total_attendees=freq.sum()
total_attendees


# In[23]:


plt.figure(figsize=(10, 6))
bars = plt.bar(freq.index, freq.values,color='skyblue')
freq.plot(kind='bar', color='skyblue')
plt.xlabel('Events')
plt.ylabel('Student Count')
plt.title('No of students attending Data Science and Related Events')
plt.xticks(rotation=45)

for i, value in enumerate(freq):
    plt.text(freq.index[i], value, f'{value}', ha='center', va='bottom')

plt.show()

