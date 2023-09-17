#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[3]:


high_cgpa_threshold=7.5
high_language_experience_threshold=5


# In[17]:


high_cgpa_exp=readxl[(readxl['CGPA']>high_cgpa_threshold)&(readxl['Experience with python (Months)']>high_language_experience_threshold)]
low_cgpa_exp=readxl[(readxl['CGPA']<=high_cgpa_threshold)&(readxl['Experience with python (Months)']<=high_language_experience_threshold)]


# In[18]:


average_salary_high_cgpa=high_cgpa_exp['Expected salary (Lac)'].mean()
average_salary_low_cgpa=low_cgpa_exp['Expected salary (Lac)'].mean()


# In[20]:


plt.figure(figsize=(8,6))
plt.bar(['High CGPA And Experience','Low CGPA and Experience'],[average_salary_high_cgpa,average_salary_low_cgpa],color=['blue','green'])
plt.xlabel('Metrics')
plt.ylabel('Average Expected Salary')
plt.title('Average Expected Salary for High CGPA and More Language Experience')
plt.xticks(rotation=0)

for i, value in enumerate([average_salary_high_cgpa,average_salary_low_cgpa]):
    plt.text(i, value, f'{value:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[ ]:




