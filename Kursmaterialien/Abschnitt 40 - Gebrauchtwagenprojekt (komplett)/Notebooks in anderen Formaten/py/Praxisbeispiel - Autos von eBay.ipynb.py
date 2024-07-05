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

# In[56]:


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

# In[74]:


import pandas as pd

df = pd.read_csv("./autos.csv.bz2", encoding = "iso8859-1")

df = df.drop(["dateCrawled", "abtest", "dateCreated", "nrOfPictures", "lastSeen", "postalCode"], axis = 1)


# In[75]:


print(len(df))


# In[76]:


#print(df["abtest"].unique())

#print(len(df[df["abtest"] == "test"]))
#print(len(df[df["abtest"] == "control"]))


# In[77]:


df.head()


# In[ ]:





