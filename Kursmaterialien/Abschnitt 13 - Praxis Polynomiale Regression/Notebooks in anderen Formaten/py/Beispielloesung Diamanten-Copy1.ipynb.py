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


# In[39]:


df.head()


# In[38]:


# Modell 1: Lineare Regression auf Basis des "carat" - Wertes

X = pd.get_dummies(df, columns = ["color"])[["x", "y", "z", "depth", "table", "carat", "color_D","color_E","color_F","color_G","color_H","color_I","color_J"]].values
Y = df[["price"]].values

import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression

scores = cross_val_score(LinearRegression(), X, Y, cv = KFold(shuffle = True))
print(np.mean(scores))


# In[33]:


# Modell 2: Lineare Regression auf Basis von Breite, Höhe und Länge

X = df[["x", "y", "z"]].values
Y = df[["price"]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[27]:


# Modell 3: Polynomiale Regression, mit Grad 2

from sklearn.linear_model import LinearRegression

X = df[["x", "y", "z"]].values
Y = df[["price"]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree = 2, include_bias = False)
pf.fit(X_train)

X_train_transformed = pf.transform(X_train)
X_test_transformed = pf.transform(X_test)

model = LinearRegression()
model.fit(X_train_transformed, y_train)

print(model.score(X_test_transformed, y_test))


# In[ ]:





# In[ ]:





