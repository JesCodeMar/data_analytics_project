#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


def categorize_income(value):
    if value < 300000:
        return 'Low'
    elif value < 700000:
        return 'Moderate'
    else:
        return 'High'


# In[3]:


excel_sheet = pd.read_excel('Data analyst Data.xlsx')


# In[4]:


excel_sheet['Family Income'] = excel_sheet['Family Income'].str.replace('[^\d.]', '', regex=True).astype(float)
excel_sheet['Family Income Category'] = excel_sheet['Family Income'].apply(categorize_income)
excel_sheet['CGPA'] = pd.to_numeric(excel_sheet['CGPA'], errors='coerce')
excel_sheet['Experience with python (Months)'] = pd.to_numeric(excel_sheet['Experience with python (Months)'], errors='coerce')


# In[5]:


selected_data = excel_sheet.dropna(subset=['Family Income Category', 'CGPA', 'Experience with python (Months)', 'Expected salary (Lac)'])


# In[6]:


plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
sns.scatterplot(x='CGPA', y='Expected salary (Lac)', data=selected_data)
plt.title('Expected Salary vs CGPA')

plt.subplot(1, 3, 2)
sns.scatterplot(x='Family Income', y='Expected salary (Lac)', data=selected_data)
plt.title('Expected Salary vs Family Income')

plt.subplot(1, 3, 3)
sns.scatterplot(x='Experience with python (Months)', y='Expected salary (Lac)', data=selected_data)
plt.title('Expected Salary vs Experience with Python')

plt.tight_layout()
plt.show()

