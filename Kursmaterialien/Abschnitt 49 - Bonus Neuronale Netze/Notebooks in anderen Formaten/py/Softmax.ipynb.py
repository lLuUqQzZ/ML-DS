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

# In[23]:


import numpy as np

np.set_printoptions(suppress=True)

def softmax(w):
    e = np.exp(np.array(w))
    dist = e / np.sum(e)
    return dist

def sigmoid(x):
    return 1 / (1 + np.exp(-np.array(x)))


# In[24]:


sigmoid([10, -2, 0, 0, 0, 0, 0, 0, 0, 0])


# In[25]:


softmax([10, -2, 0, 0, 0, 0, 0, 0, 0, 0])


# In[26]:


softmax([1, -0.2, 0, 0, 0, 0, 0, 0, 0, 0])


# In[ ]:





