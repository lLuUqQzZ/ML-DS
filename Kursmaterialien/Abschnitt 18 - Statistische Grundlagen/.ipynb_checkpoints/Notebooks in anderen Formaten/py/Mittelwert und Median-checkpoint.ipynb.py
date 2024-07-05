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

# In[10]:


import numpy as np

incomes = [10000, 30000, 5000000]


# In[11]:


np.median(incomes)


# In[12]:


np.mean(incomes)


# In[13]:


import pandas as pd

df = pd.read_csv("./diamonds.csv")

df.head()


# In[14]:


df["carat"].mean()


# In[15]:


df["carat"].median()


# In[16]:


df.mean()


# In[17]:


df.median()


# In[ ]:





