#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[20]:


readxl['Year of Graduation'] = pd.to_numeric(readxl['Year of Graduation'], errors='coerce')
students_graduating=readxl.dropna(subset=['Year of Graduation'])


# In[21]:


print(readxl['Year of Graduation'].unique())


# In[26]:


graduation_year_counts = students_graduating['Year of Graduation'].value_counts().sort_index()
graduation_year_counts


# In[25]:


plt.figure(figsize=(10, 6))
bars = plt.bar(graduation_year_counts.index, graduation_year_counts.values, color='red', alpha=0.7)

for bar in bars:
    if bar.get_height() == graduation_year_counts[2024]:
        bar.set_color('green')

plt.xlabel('Year of Graduation')
plt.ylabel('Number of Students')
plt.title('Number of Students by Graduation Year')
plt.xticks(graduation_year_counts.index, rotation=45)

for i, value in enumerate(graduation_year_counts):
    plt.text(graduation_year_counts.index[i], value, f'{value}', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[ ]:




