#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv('forbes_richman.csv', encoding='ISO-8859-1')


# In[6]:


# to get the first 10 values
df.head(10)


# In[7]:


# to get the shape of the dataframe
df.shape


# In[8]:


# to sum count the null value in each column
df.isnull().sum()


# In[9]:


# to calculate the mean, max, std, count of the numeric values
df.describe()


# In[10]:


# count duplicate values
df.duplicated().sum()


# In[11]:


# count distinct value in each column
df['Name'].value_counts()


# In[12]:


df.info()


# In[13]:


# shows the column names
df.columns


# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


# count each value in a column
df.count()


# In[ ]:





# In[15]:


df.notnull().sum()


# In[16]:


# counts all the rows with null value in a column
df.isnull().sum()


# In[ ]:





# In[ ]:





# In[17]:


df.apply(pd.to_numeric, errors = 'ignore')


# In[18]:


# fill in 0 to all the rows with nan in age column
df['Age'] = df['Age'].fillna(0)


# In[19]:


# removing allthe rows with nan 
not_null_roll = df.notnull().all(axis=1)
data = df[not_null_roll]
data


# In[20]:


# checking for null values
data.isnull().sum()


# In[21]:


# converting 'Age' column to integer
data['Age'] = data['Age'].astype(int)


# In[22]:


data


# In[23]:


# sorting the data to know the person with the highest networth
data.sort_values(by='Net Worth', ascending=False).head(10)


# In[24]:


# sorting data to know the person with the lowest networth
data.sort_values(by='Net Worth', ascending=True).head(10)


# In[ ]:





# In[ ]:





# In[ ]:




