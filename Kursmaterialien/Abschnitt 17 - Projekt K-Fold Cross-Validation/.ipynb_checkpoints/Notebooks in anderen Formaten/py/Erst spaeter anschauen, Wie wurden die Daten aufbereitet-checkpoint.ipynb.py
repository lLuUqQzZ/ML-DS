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

# In[2]:


import pandas as pd

df = pd.read_csv("../data/autos.csv", encoding="ISO-8859-1")

df.head()


# In[4]:


df = df[["price", "yearOfRegistration", "powerPS", "kilometer", "model", "fuelType", "name", "gearbox"]]

# Dann filtern wir unrealistische Daten heraus
df = df[df["price"] < 50000]
df = df[df["price"] > 0]
df = df[df["powerPS"] < 300]
df = df[df["powerPS"] > 30]
df = df[df["yearOfRegistration"] < 2020]
df = df[df["yearOfRegistration"] > 1970]

# Einen Kilometerstand von 150.000km haben erstaunlich viele Autos. Theorie: Autos mit 300.000km werden auch unter 150.000km geführt
df = df[df["kilometer"] <= 140000]


# In[5]:


df.to_csv("./autos_cross_val.csv.bz2", compression = "bz2", index = False)


# In[ ]:





# In[ ]:





