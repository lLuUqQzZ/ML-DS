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

# # PCA zum Komprimieren von Daten
# 
# Datenquelle: https://www.kaggle.com/uciml/human-activity-recognition-with-smartphones/data

# In[1]:


import pandas as pd

train = pd.read_csv("./train.csv.bz2")
test = pd.read_csv("./test.csv.bz2")


# In[2]:


X_train = train.drop("subject", axis = 1).drop("Activity", axis = 1)
y_train = train["Activity"]

X_test = test.drop("subject", axis = 1).drop("Activity", axis = 1)
y_test = test["Activity"]

from sklearn.preprocessing import StandardScaler

s = StandardScaler()
X_train = s.fit_transform(X_train)
X_test = s.transform(X_test)


# In[3]:


from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

import numpy as np


# In[14]:




# In[15]:




# In[ ]:





