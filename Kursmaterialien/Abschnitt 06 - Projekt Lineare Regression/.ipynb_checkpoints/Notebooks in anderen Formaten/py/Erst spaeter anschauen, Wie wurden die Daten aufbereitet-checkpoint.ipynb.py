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

# # <span style="color:red">Wichtiger Hinweis: Dieses Notebook erst später anschauen!</span>
# 
# ### Dieses Notebook zeigt dir, wie ich die Daten aufbereitet habe. Dabei verwende ich aber Funktionen, die du zum aktuellen Zeitpunkt noch nicht kennst. 
# 
# ### Dieses Notebook dient primär der Vollständigkeit - und damit du dich (nach Abschluss des Kurses) überzeugen kannst, dass es sich bei den Daten tatsächlich um echte Daten handelt ;) 
# 
# ### Ich empfehle dir, dieses Notebook dir erst später im Verlauf des Kurses nochmal anzuschauen!
# 

# In[25]:


# Datenquelle: https://www.kaggle.com/orgesleka/used-cars-database

import pandas as pd

df = pd.read_csv("./../data/autos.csv", encoding="iso-8859-1")
df.head()


# In[26]:


# Zuerst wählen wir die Spalten aus, die uns tatsächlich interessieren

df = df[["price", "yearOfRegistration", "powerPS", "kilometer", "model", "fuelType", "name"]]


# In[27]:


# Dann filtern wir unrealistische Daten heraus
df = df[df["price"] < 50000]
df = df[df["powerPS"] < 300]
df = df[df["powerPS"] > 30]
df = df[df["yearOfRegistration"] < 2020]
df = df[df["yearOfRegistration"] > 1970]

# Einen Kilometerstand von 150.000km haben erstaunlich viele Autos. Theorie: Autos mit 300.000km werden auch unter 150.000km geführt
df = df[df["kilometer"] <= 140000]

# Dann nehmen wir eine Stichprobe (250 Autos) aus der Datei heraus
# Dadurch können wir später den Rest einfacher visualisieren und das Diagramm ist nicht "überfüllt"
df = df.sample(250)


# In[28]:


# Und speichern es als .csv - Datei
df.to_csv("./autos_prepared.csv", index = False)


# In[29]:


print(len(df))


# In[30]:


df.head()


# In[31]:


from sklearn.linear_model import LinearRegression
d = df.sample(250)

X = d[["kilometer"]].values
Y = d[["price"]].values

model = LinearRegression()
model.fit(X, Y)


# In[32]:


import matplotlib.pyplot as plt

plt.scatter(X, Y)
# plt.plot([[0], [300]], model.predict([[0], [300]]))
plt.show()


# In[33]:


# Test, ob wir coole Ergebnisse dann später auch herausbekommen ;) 

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, Y)

model.predict([[10000], [100000]])


# In[ ]:





# In[ ]:





