#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[3]:


college_event_counts = readxl[readxl['How did you come to know about this event?'] == 'SPOC/ College Professor']


# In[4]:


college_event_counts = college_event_counts['College Name'].value_counts().reset_index()
college_event_counts.columns = ['College Name', 'Number of Students']


# In[5]:


top_5_colleges = college_event_counts.nlargest(5, 'Number of Students')


# In[6]:


plt.figure(figsize=(10, 6))
sns.set_palette("pastel")
ax = sns.barplot(y='Number of Students', x='College Name', data=top_5_colleges)

plt.title("Students Who Know About the Event from Top 5 Colleges")
plt.ylabel("Number of Students")
plt.xlabel("College Name")

plt.xticks(range(len(top_5_colleges)), top_5_colleges['College Name'], rotation=45, ha='right')

plt.yticks(range(0, top_5_colleges['Number of Students'].max() + 1, 10))

for index, row in top_5_colleges.iterrows():
    plt.annotate(str(row['Number of Students']), xy=(index, row['Number of Students']),ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()


# In[ ]:




