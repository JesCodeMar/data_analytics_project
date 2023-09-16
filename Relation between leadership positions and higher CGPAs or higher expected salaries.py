#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[6]:


readxl['Expected salary (Lac)']=pd.to_numeric(readxl['Expected salary (Lac)'],errors='coerce')
readxl['Leadership- skills']=readxl['Leadership- skills'].str.strip()
readxl['CGPA'] = pd.to_numeric(readxl['CGPA'], errors='coerce')


# In[7]:


print(readxl['Expected salary (Lac)'].unique())


# In[8]:


selected_data = readxl.dropna(subset=['CGPA', 'Expected salary (Lac)','Leadership- skills'])


# In[11]:


plt.figure(figsize=(10, 6))
plot = sns.scatterplot(x='Leadership- skills', y='CGPA', hue='Expected salary (Lac)', data=readxl, palette='coolwarm', s=50, alpha=0.7)

plt.xlabel('Leadership Skills', fontsize=12)
plt.ylabel('CGPA', fontsize=12)

legend = plot.legend(title='Expected Salary (Lac)')
legend_labels = ['5 Lakhs', '7 Lakhs', '10 Lakhs', '14 Lakhs', '15 Lakhs','30 Lakhs','35 Lakhs']
for text, label in zip(legend.texts, legend_labels):
    text.set_text(label)

plt.tight_layout()
plt.show()

