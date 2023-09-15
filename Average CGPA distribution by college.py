#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt


# In[19]:


readxl=pd.read_excel('Data analyst Data.xlsx')
df=pd.DataFrame(readxl)


# In[23]:


average_gpa_by_college = df.groupby('College Name')['CGPA'].mean().sort_values(ascending=False)


# In[30]:


average_gpa_by_college.dropna(inplace=True)
college_show=average_gpa_by_college.head()
college_show


# In[40]:


college=college_show.to_dict()
College_name=list(college.keys())
College_CGPA=list(college.values())
listco=list(zip(College_name, College_CGPA))
df1 = pd.DataFrame(listco,columns=['Name of College', 'Average CGPA'])
df1


# In[ ]:




