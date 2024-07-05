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

# In[1]:


import numpy as np

n = 200

width = abs(np.random.normal(1000, 500, n))
length = abs(np.random.normal(500, 300, n))

profit = width ** 1.9 + np.random.normal(100000, 50000, n)


# In[2]:


import pandas as pd

df = pd.DataFrame({
    "width": width,
    "length": length,
    "profit": profit
})


# In[3]:


df = df.round()


# In[4]:


df.to_csv("./fields.csv", index = False)


# In[5]:


X = df[["width", "length"]].values
Y = df[["profit"]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
print(model.coef_)


# In[6]:


X = df[["width", "length"]].values
Y = df[["profit"]].values

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

from sklearn.linear_model import LinearRegression

pf = PolynomialFeatures()
pf.fit(X_train)

model = LinearRegression()
model.fit(pf.transform(X_train), y_train)

print(model.score(pf.transform(X_test), y_test))


# In[ ]:


from sklearn.svm import SVR

model = SVR(kernel = "poly", degree = 2, verbose = True)
model.fit(X_train, y_train.reshape(-1))

print(model.score(X_test, y_test.reshape(-1)))


# In[ ]:


from sklearn.svm import SVR

model = SVR(kernel = "poly", verbose = True)
model.fit(X_train, y_train.reshape(-1))

print(model.score(X_test, y_test.reshape(-1)))


# In[ ]:





