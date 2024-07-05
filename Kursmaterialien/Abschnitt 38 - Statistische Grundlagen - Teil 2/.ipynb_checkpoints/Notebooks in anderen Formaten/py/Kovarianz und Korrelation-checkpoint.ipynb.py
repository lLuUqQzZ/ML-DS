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

# In[2]:


import pandas as pd
import numpy as np

df = pd.read_csv("./classification.csv")
df["extra"] = np.random.normal(5, 16, len(df))

df.head()


# In[14]:


df.cov()


# In[5]:


df.corr()


# In[7]:


x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 1, 0, 0, 0, 1, 1]


# In[8]:


np.cov(x, y)


# In[12]:


np.corrcoef(x, y)


# In[ ]:





# In[ ]:





