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

# In[11]:


import numpy as np


# In[12]:


np.where([True, False], [1, 2], [3, 4])


# In[13]:


noten = np.array([1, 2, 3, 4, 5, 6])


# In[15]:


print(noten <= 4)


# In[16]:


np.where(noten <= 4, "bestanden", "nicht bestanden")


# In[17]:


import pandas as pd

df = pd.read_csv("diamonds.csv")

# https://www.kaggle.com/shivam2503/diamonds/data
# Color: from J (worst) to D (best)

# Idee: Wir fassen die Spalte "color" zusammen. 
# Aus einem D wird eine 1,
# aus allen anderen wird eine 0


# In[19]:


df.head()


# In[23]:


df["color"] = np.where(df["color"] == "D", 1, 0)


# In[25]:


df.head()


# In[26]:


df["cut"] = np.where(df["cut"] == "Premium", "Premium++", df["cut"])


# In[27]:


df.head()


# In[ ]:





