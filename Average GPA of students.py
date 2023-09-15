#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[3]:


df=pd.DataFrame(readxl)


# In[9]:


student=df[df['Designation'].str.strip().str.lower().str.contains('student')].copy()
student.dropna(subset=['CGPA'],inplace=True)
student_average_cgpa=student['CGPA'].mean()


# In[11]:


print("Average student cgpa: ", student_average_cgpa)

