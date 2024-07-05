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

df = pd.read_csv("./hotels.csv")

df.head()


# In[3]:


X = df[["Gewinn", "Quadratmeter"]].values
Y = df[["Preis in Mio"]].values


# In[4]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)


# In[5]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)


# In[6]:


print(model.intercept_)


# In[7]:


print(model.coef_)


# In[8]:


# 6.48370247 + [Gewinn] * 6.39855984e-06 + [Quadrameter] * 3.89642288e-03


# In[9]:


y_test_pred = model.predict(X_test)


# In[10]:


for i in range(0, len(y_test_pred)):
    print(str(y_test_pred[i][0]) + " - " + str(y_test[i][0]))


# In[1]:


y_test


# In[ ]:





