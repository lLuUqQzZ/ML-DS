# Diese .py - Datei wurde automatisch aus dem IPython - Notebook (.ipynb) generiert.
# 
# Gelegentlich wurde ich von Teilnehmern gefragt, ob ich die Kursmaterialien nicht 
# auch als normale .py - Datien bereitstellen könne. Dadurch ist es möglich, den Code
# ohne Jupyter zu öffnen, beispielsweise wenn Python-Programme in einem Terminal oder in 
# Eclipse entwickelt werden.
# 
# Dem möchte ich hiermit nachkommen. Ich empfehle dir aber trotzdem, schau' dir lieber die
# IPython - Notebooks direkt an, oder den HTML-Export eben dieser. Dieser reine .py-Export
# ist meiner Meinung nach etwas unübersichtlich.
# 
# Bitte beachte zudem, dass du Pfadangaben ggf. manuell korrigieren musst!
# 
#!/usr/bin/env python
# coding: utf-8

# ## Numpy kann auch Matritzen!

# In[1]:


import numpy as np

np.array([[1, 2, 3], [4, 5, 6]])


# In[3]:


m = np.array([[1, 2, 3], [4, 5, 6]])

print(m.shape)


# In[10]:


np.ones((2, 3))


# In[11]:


np.zeros((2, 3))


# In[14]:


np.arange(1, 7).reshape(3, 2)


# In[15]:


m = np.array([[1, 2, 3], [4, 5, 6]])

print(m)


# In[20]:


m.reshape(6)


# In[22]:


np.arange(1, 7).reshape(2, -1)


# In[32]:


np.arange(1, 7).reshape(-1, 2)


# In[28]:


m = np.array([[1, 2, 3], [4, 5, 6]])

print(m.reshape(-1))


# In[33]:




# In[ ]:





