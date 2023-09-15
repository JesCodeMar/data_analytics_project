#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[3]:


df=pd.DataFrame(readxl)


# In[13]:


student=df[df['Designation'].str.strip().str.lower().str.contains('student')].copy()
student.dropna()
print(student['Experience with python (Months)'].unique())


# In[21]:


std_exp1=student[student['Experience with python (Months)']==3]
std_exp2=student[student['Experience with python (Months)']==4]
std_exp3=student[student['Experience with python (Months)']==5]
std_exp4=student[student['Experience with python (Months)']==6]
std_exp5=student[student['Experience with python (Months)']==7]
std_exp6=student[student['Experience with python (Months)']==8]

std1len=len(std_exp1)
std2len=len(std_exp2)
std3len=len(std_exp3)
std4len=len(std_exp4)
std5len=len(std_exp5)
std6len=len(std_exp6)


# In[22]:


no_of_months=[3,4,5,6,7,8]
count=[std1len,std2len,std3len,std4len,std5len,std6len]
listofcounts=list(zip(no_of_months, count))
df1 = pd.DataFrame(listofcounts,columns=['No of months of experience', 'No of students'])
df1


# In[32]:


plt.bar(df1['No of months of experience'], df1['No of students'], width=0.5, align='center')

plt.xlabel('No of months of experience')
plt.ylabel('No of students')
plt.title('Distribution of students experience with python programming')

plt.show()

