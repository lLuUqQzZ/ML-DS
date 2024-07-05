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

# In[3]:


import pandas as pd
import numpy as np

df = pd.read_csv("./autos.csv.bz2", encoding = "iso8859-1")

# Zuerst entfernen wir Spalten, die für unser Modell keine Aussagekraft haben sollten
df = df.drop(["dateCrawled", "abtest", "dateCreated", "nrOfPictures", "lastSeen", "postalCode", "seller", "offerType"], axis = 1)

# Hier berechnen wir die Spalte "registration", sodass das Jahr als Kommazahl repräsentiert wird 
df["monthOfRegistration"] = np.where(df["monthOfRegistration"] == 0, 6, df["monthOfRegistration"])
df["registration"] = df["yearOfRegistration"] + (df["monthOfRegistration"] - 1) / 12
df = df.drop(["yearOfRegistration", "monthOfRegistration"], axis = 1)

# Wir entfernen alle Einträge, wo die Spalte "price" oder "powerPS" auf 0 ist
df = df.drop(df[df["price"] == 0].index)
df = df.drop(df[df["powerPS"] == 0].index)

df.head()


# In[4]:


df["notRepairedDamage"].unique()


# In[5]:


df["notRepairedDamage"] = np.where(df["notRepairedDamage"] == "ja", 1, df["notRepairedDamage"])
df["notRepairedDamage"] = np.where(df["notRepairedDamage"] == "nein", 0, df["notRepairedDamage"])


# In[6]:


df = df[df["notRepairedDamage"].notnull()]


# In[7]:


df.head()


# In[8]:


df = df[(df["price"] < 50000) & (df["powerPS"] < 500) & (df["registration"] <= 2018)]


# In[10]:


import seaborn as sns

g = sns.pairplot(df.sample(250), hue="fuelType")


# In[11]:


g = sns.pairplot(df.sample(250), hue="gearbox")


# In[16]:


g = sns.pairplot(df.sample(250), hue="vehicleType")


# In[ ]:





