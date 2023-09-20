#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy as sp


# In[2]:


#Data interpretation


# In[3]:


ll = [[1,2,3,4,5,6],[3,4,5,6,7,8]]
np.mean(ll) #Calculate the mean value of all elements


# In[4]:


np.mean(ll,0) #Calculate the mean value by column.The value 0 indicates the column vector.


# In[5]:


np.mean(ll,1) #Calculate the mean value by row.The value 1 indicates the row vector.


# In[ ]:




