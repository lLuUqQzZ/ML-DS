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


import pandas as pd

df = pd.read_csv("./hotels.csv")

df = pd.get_dummies(df, columns = ["Stadt"])

df.head()


# In[2]:


Y = df[["Preis in Mio"]].values


# In[3]:


# Option 1: Explizit auflisten, welche Spalten wir in X haben möchten
X = df[["Gewinn", "Quadratmeter", "Stadt_Berlin", "Stadt_Köln"]].values

# Option 2: Explizit auflisten, welche Spalten wir **nicht** in X haben möchten
# df.drop(labels = ["Preis in Mio", "Stadt_München"], axis = 1).values


# In[5]:


# Train / Test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)

# Lineare Regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[13]:


model.predict([[10000, 300, 0, 0], [10000, 300, 1, 0], [10000, 300, 0, 1]])


# In[ ]:





