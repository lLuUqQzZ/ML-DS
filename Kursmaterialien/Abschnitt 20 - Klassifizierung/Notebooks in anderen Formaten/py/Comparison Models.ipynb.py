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


from sklearn.model_selection import train_test_split

import numpy as np

import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[4]:


X = df[["education", "interview"]].values

y = df["success"].values


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)


# In[18]:


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

models = {
    "logistic regression": LogisticRegression(),
    "svc": SVC(),
    "neural network": MLPClassifier(),
    "decition tree": DecisionTreeClassifier(),
    "random forest": RandomForestClassifier(),
    "gradient boosting": GradientBoostingClassifier()
}

for key, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(key + ": " + str(score))


# In[25]:


import matplotlib.pyplot as plt

plt.scatter(X_train[:, 0], X_train[:, 1], c = y_train)
plt.show()


# In[26]:


import matplotlib.pyplot as plt

plt.contourf()
plt.scatter(X_test[:, 0], X_test[:, 1], c = y_test)
plt.show()


# In[ ]:





