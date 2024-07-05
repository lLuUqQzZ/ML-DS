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

# In[38]:


import pandas as pd

df = pd.read_csv("./fields.csv")


# In[39]:


df.head()


# In[40]:


# Beispiel: Normale, lineare Regression

X = df[["width", "length"]].values
Y = df[["profit"]].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 42, test_size = 0.25)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[32]:


from sklearn.preprocessing import PolynomialFeatures



# In[67]:


pf = PolynomialFeatures(degree = 2, include_bias = False)
pf.fit(X_train)

X_train_transformed = pf.transform(X_train)[:, [0, 2]]
X_test_transformed = pf.transform(X_test)[:, [0, 2]]

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train_transformed, y_train)

print(model.score(X_test_transformed, y_test))


# In[68]:


print(pf.powers_)
# width ^ 1 + length ^ 0
# width ^ 2 + length ^ 0


# In[ ]:





# In[ ]:





