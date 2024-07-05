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

# ## Validation-Curve
# 
# Berechne die Validation-Curve für einen DecisionTreeClassifier, und bestimme so den idealen `max_depth` - Parameter für den Entscheidungsbaum.

# In[1]:


import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[2]:


X = df[["age", "interest"]].values
y = df["success"].values


# In[3]:


# Wird eigentlich nicht benötigt - setzt aber ein paar
# parktische Matplotlib-Eigenschaften, damit die Grafik
# in einer höheren Auflösung generiert wird
import helper


# In[4]:


from sklearn.model_selection import validation_curve
from sklearn.tree import DecisionTreeClassifier

import numpy as np

param_range = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

train_scores, test_scores = validation_curve(
    DecisionTreeClassifier(), 
    X,
    y,
    param_name = "max_depth",
    param_range=param_range)


# In[5]:


import matplotlib.pyplot as plt

plt.plot(param_range, np.mean(train_scores, axis = 1))
plt.plot(param_range, np.mean(test_scores, axis = 1))

# Hiermit drehen wir die X-Achse um, sie geht jetzt von 40 bis 1.
# plt.xlim(np.max(param_range), 0)

plt.show()


# In[ ]:





# In[ ]:





