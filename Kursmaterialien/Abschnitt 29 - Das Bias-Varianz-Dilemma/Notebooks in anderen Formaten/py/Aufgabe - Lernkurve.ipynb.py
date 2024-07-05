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
# 
# Berechne die Lernkurve für einen `RandomForestClassifier` (mit Standard-Parametern). Würde es sich für dieses Modell lohnen, noch zusätzliche Daten zu sammeln? 

# In[2]:


import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[3]:


X = df[["age", "interest"]].values
y = df["success"].values


# In[1]:


# Wird eigentlich nicht benötigt - setzt aber ein paar
# parktische Matplotlib-Eigenschaften, damit die Grafik
# in einer höheren Auflösung generiert wird
import helper


# In[ ]:





# In[ ]:





