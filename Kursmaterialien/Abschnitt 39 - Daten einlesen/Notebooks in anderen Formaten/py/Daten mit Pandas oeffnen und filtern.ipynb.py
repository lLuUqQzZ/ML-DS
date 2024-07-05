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

# In[3]:


import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[10]:


df[df["age"] > 20]


# In[13]:


# OR: df[(df["age"] > 20) | (df["age"] < 30)]
df[(df["age"] > 20) & (df["age"] < 30)] # AND


# In[19]:


df.drop([1, 3]).head()


# In[22]:


success = df[df["success"] == 1]
success.head()


# In[23]:


success.index


# In[25]:


df.drop(success.index).head()


# In[ ]:





# In[ ]:





