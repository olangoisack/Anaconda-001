#!/usr/bin/env python
# coding: utf-8

# <h1 style="font-size:3rem;color:orange;"Jupyter Notebook

# <h1 style="font-size:3rem;color:orange;">Jupyter Notebook Tutorial</h1>

# # Python for Beginners

# <img scr="https://picsum.photos/id/0/400/400">

# <img scr="https://picsum.photos/id/0/400/400">

# ## Basic Output

# In[2]:


print('Hello World!')


# ## Insert Variable into a string




person = input("What's your name?")
message = "Hello, {}!".format(person)
print(message)


# ## Multiline Strings and String Length

# In[8]:


story = """Once upon a time 
there lived a bear family
who ate delicious pizza"""
print(story)
print(len(story))


# ## Math Operations

# In[9]:


x = 7
y = 4
z=(x * 3) / y
m = (x * 3) % y #modulo returns the remainder
print(z)
print(m)


# ## Lists (arrays)
# 

# In[11]:


friends = ['Monica', 'Phoebe', 'Rachel','Chandler','Joey','Ross']
print(friends[0])


# In[ ]:




