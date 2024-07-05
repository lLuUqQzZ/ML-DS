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

# In[18]:


import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[3]:


df[df["age"] < 18].head()


# In[6]:


# df["age"] = 19
df.head()


# In[15]:


import numpy as np

print(np.where([True, False], [1, 2], [3, 4]))
print(np.where([True, False], 1, 2))


# In[19]:


df["age2"] = np.where(df["age"] < 18, "minderjährig", "volljährig")


# In[20]:


df.head()


# In[21]:


df["interest"] = df["interest"] * 5


# In[22]:


df.head()


# In[ ]:





