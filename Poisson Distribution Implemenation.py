#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


#Generate 10,000 numbers that comply with the Poisson distribution where the value of lambda is 2



# In[7]:


X=np.random.poisson(lam=2,size=10000)


# In[4]:


a=plt.hist(X,bins=15,range=[0,15])
#Generate grids.
plt.grid()
plt.show()

