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

# In[4]:


import pandas as pd

df = pd.read_csv("./hotels.csv")

df = pd.get_dummies(df, columns = ["Stadt"])

df.head()


# In[5]:


Y = df[["Preis in Mio"]].values


# In[11]:


# Option 1: Explizit auflisten, welche Spalten wir in X haben möchten
X = df[["Gewinn", "Quadratmeter", "Stadt_Berlin", "Stadt_Köln"]].values

# Option 2: Explizit auflisten, welche Spalten wir **nicht** in X haben möchten
# df.drop(labels = ["Preis in Mio", "Stadt_München"], axis = 1).values


# In[ ]:





# In[ ]:





