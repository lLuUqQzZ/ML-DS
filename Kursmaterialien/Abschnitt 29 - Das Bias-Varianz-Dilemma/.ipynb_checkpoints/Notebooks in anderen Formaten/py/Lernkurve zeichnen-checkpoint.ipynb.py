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

# ## Lernkurve

# In[1]:


import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[14]:


X = df[["age", "interest"]].values
y = df["success"].values


# In[15]:


# Wird eigentlich nicht benötigt - setzt aber ein paar
# parktische Matplotlib-Eigenschaften, damit die Grafik
# in einer höheren Auflösung generiert wird
import helper


# In[104]:


from sklearn.model_selection import learning_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle

import numpy as np

X, y = shuffle(X, y)

train_sizes_abs, train_scores, test_scores = learning_curve(LogisticRegression(), X, y)


# In[105]:



import matplotlib.pyplot as plt

plt.plot(train_sizes_abs, np.mean(train_scores, axis = 1))
plt.plot(train_sizes_abs, np.mean(test_scores, axis = 1))

plt.show()


# In[ ]:





# In[ ]:





