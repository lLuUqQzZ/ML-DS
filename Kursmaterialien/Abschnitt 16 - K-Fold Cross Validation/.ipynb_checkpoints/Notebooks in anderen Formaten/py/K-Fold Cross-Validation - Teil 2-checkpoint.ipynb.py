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

# In[5]:


import pandas as pd

df = pd.read_csv("./hotels.csv")[:6]

df


# In[7]:


X = df[["Gewinn", "Quadratmeter"]].values
Y = df[["Preis in Mio"]].values


# In[15]:


X


# In[17]:


X[[0, 4]]


# In[10]:


from sklearn.model_selection import KFold

kf = KFold()

for train_index, test_index in kf.split(X):
    print("train: " + str(train_index))
    print("test: " + str(test_index))
    print("-----------")
    X_test = X[test_index]
    X_train = X[train_index]
    
    y_test = Y[test_index]
    y_train = Y[train_index]


# In[ ]:





