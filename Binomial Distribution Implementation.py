#!/usr/bin/env python
# coding: utf-8

# In[23]:


from scipy.stats import binom,norm,beta,expon


# In[24]:


import numpy as np
import matplotlib.pyplot as plt


# In[25]:


#The n and p parameters indicates the success times and probability in the binomial formula,respectively,and size indicates the number of sampling times.


# In[26]:


binom_sim = binom.rvs(n=10,p=0.3,size=10000)
print('Data:',binom_sim)
print('Mean: %g' % np.mean(binom_sim))
print('SD: %g' % np.std(binom_sim,ddof=1))


# In[27]:


#Generate a histogram.The bins parameter indicates the number of bars in total.By default,the sum of the percentages of al bars is 1.


# In[9]:


plt.hist(binom_sim, bins=10)
plt.xlabel(('x'))
plt.ylabel('density')
plt.show()

