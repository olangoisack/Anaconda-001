#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Data preparation


# In[11]:


import numpy as np


# In[12]:


b=[1,3,5,6]


# In[13]:


ll=[[1,2,3,4,5,6],[3,4,5,6,7,8]]



# In[14]:


#Calculate the variance


# In[15]:


np.var(b)


# In[16]:


np.var(ll,1)  #The value of the second parameter is 1,indicating that the variance is calculated by row


# In[ ]:




