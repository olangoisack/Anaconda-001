#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


mu=0
sigma = 1


# In[3]:


#Return evenly spaced values within a given interval(start,stop,step).


# In[4]:


x = np.arange(-5,5,0.1)


# In[5]:


#Generate normal distribution that complies with mu and sigma.


# In[6]:


y= norm.pdf(x,mu,sigma)


# In[7]:


plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('density')
plt.show()


# In[ ]:




