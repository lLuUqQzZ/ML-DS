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


# Originalquelle der Daten: https://www.kaggle.com/orgesleka/used-cars-database

# Damit ihr euch dort aber nicht registrieren müsst, habe ich mich entschlossen,
# diese auf meinem eigenen Webspace zu hosten. 

import urllib3

url = "http://downloads.codingcoursestv.eu/035%20-%20machine%20learning/data/autos.csv.bz2"

http = urllib3.PoolManager()
download = http.urlopen("GET", url, preload_content = False)  
data = download.read()

with open('autos.csv.bz2', 'wb') as f:  
    f.write(data)


# ### Ziel: Wir möchten ein Modell entwickeln, welches für *gewöhnliche* Autos den Verkaufspreis schätzen kann

# In[42]:


import pandas as pd
import numpy as np

df = pd.read_csv("./autos.csv.bz2", encoding = "iso8859-1")

# Zuerst entfernen wir Spalten, die für unser Modell keine Aussagekraft haben sollten
df = df.drop(["dateCrawled", "abtest", "dateCreated", "nrOfPictures", "lastSeen", "postalCode", "seller", "offerType"], axis = 1)

# Hier berechnen wir die Spalte "registration", sodass das Jahr als Kommazahl repräsentiert wird 
df["monthOfRegistration"] = np.where(df["monthOfRegistration"] == 0, 6, df["monthOfRegistration"])
df["registration"] = df["yearOfRegistration"] + (df["monthOfRegistration"] - 1) / 12
df = df.drop(["yearOfRegistration", "monthOfRegistration"], axis = 1)

df.head()


# In[44]:


# df["seller"].unique()


# In[45]:


# len(df[df["seller"] == "gewerblich"])


# In[46]:


# len(df[df["seller"] == "privat"])


# In[47]:


# df["seller"].describe()


# In[48]:


# df["offerType"].describe()


# In[49]:


df.head()


# In[56]:


df = df.drop(df[df["price"] == 0].index)
df = df.drop(df[df["powerPS"] == 0].index)

# Filtern mit einem OR: df[(df["powerPS"] == 0) | (df["price"] == 0)]
# Filtern mit einem AND: df[(df["powerPS"] == 0) & (df["price"] == 0)]

# df = df.drop(df[(df["powerPS"] == 0) | (df["price"] == 0)].index)


# In[57]:


df.head()


# In[ ]:





