#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as mpt


# In[3]:


readxl=pd.read_excel('Data analyst Data.xlsx')


# In[4]:


df=pd.DataFrame(readxl)


# In[7]:


df.rename(columns={'Email ID':'email_id'},inplace=True)


# In[8]:


df.email_id.nunique(dropna=True)


# In[ ]:




