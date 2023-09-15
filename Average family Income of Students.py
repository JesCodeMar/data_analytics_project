#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[3]:


df=pd.DataFrame(readxl)


# In[18]:


student=df[df['Designation'].str.strip().str.lower().str.contains('student')].copy()
student.dropna()
print(student['Family Income'].unique())


# In[19]:


std_inc1=student[student['Family Income']=='0-2 Lakh']
std_inc2=student[student['Family Income']=='2-5 Lakh']
std_inc3=student[student['Family Income']=='5-7 Lakh']
std_inc4=student[student['Family Income']=='7 Lakh+']

std1len=len(std_inc1)
std2len=len(std_inc2)
std3len=len(std_inc3)
std4len=len(std_inc4)


# In[21]:


income_range=["0-200000","200000-500000","500000-700000","700000+"]
frequencies=[std1len,std2len,std3len,std4len]

def calculate_midpoint(range_str):
    if "+" in range_str:
        return int(income_range[income_range.index(range_str) - 1].split('-')[1])
    else:
        start, end = map(int, range_str.split('-'))
        return (start + end) / 2
weighted_sum = sum(f * calculate_midpoint(range_str) for f, range_str in zip(frequencies, income_range))
total_data_points = sum(frequencies)
overall_average_salary = weighted_sum / total_data_points
print("Overall average family income:", overall_average_salary)


# In[ ]:




