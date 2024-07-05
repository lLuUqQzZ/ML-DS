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

df = pd.read_csv("./diamonds.csv")

df.head()


# In[5]:


X = df[["carat"]].values
Y = df[["price"]].values

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, RepeatedKFold

scores = cross_val_score(LinearRegression(), X, Y, cv = RepeatedKFold())

import numpy as np

print(np.mean(scores))


# In[13]:


X = df[["x", "y", "z"]].values
Y = df[["price"]].values

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, RepeatedKFold

scores = cross_val_score(LinearRegression(), X, Y, cv = RepeatedKFold(n_repeats = 1000))

import numpy as np

print(np.mean(scores))


# In[12]:





# In[ ]:





