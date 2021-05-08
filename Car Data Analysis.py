#!/usr/bin/env python
# coding: utf-8

# # Car Dataset Analysis project

# In[2]:


import pandas as pd


# In[4]:


car = pd.read_csv(r"C:\Users\Admin\Desktop\CarsData1.csv")  #import Data


# In[6]:


car.head() #1st 5 rows of data


# In[7]:


car.shape #Row and column number of the given data


# In[8]:


car.isnull() #Number of null values


# In[10]:


car.isnull().sum() #Every columns total null value number


# In[14]:


car['Cylinders'].fillna(car['Cylinders'].mean()) # Fill null values with the mean of the column


# In[15]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True) #To update data in the main sheet


# In[16]:


car


# In[18]:


car['Make'].value_counts() #All the car making company name 


# In[19]:


car['Make'].shape


# In[23]:


car[car['Origin'].isin(['Asia','Europe'])] #Show the Origin of asia and Europe


# In[24]:


car['Weight']>4000


# In[25]:


car[car['Weight']>4000]


# In[26]:


car[~(car['Weight']>4000)] #Remove rows where weight>4000


# In[27]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3) #Increasing the value of MPG_City column value by 3


# In[28]:


car


# In[ ]:




