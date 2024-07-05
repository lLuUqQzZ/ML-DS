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

# Daten einlesen 
#  -> Quelle: http://world.openfoodfacts.org/data/en.openfoodfacts.org.products.csv
# 
# Diese Datei musst du natürlich herunterladen, damit dieses Script
# hier ausgeführt werden kann. Aber Achtung: Ca. 1.5GB!
df = pd.read_csv("en.openfoodfacts.org.products.csv", delimiter = "\t")

# Und filtern...
df = df[df["product_name"].notnull()]
df = df[df["categories_en"].notnull()]


# In[3]:


apple = df[(df["product_name"].str.contains("Juice")) & (df["product_name"].str.contains("Apple")) & (~df["product_name"].str.contains("Pineapple")) & df["categories_en"].str.contains("Fruit-based beverages")].copy()
apple["clss"] = "Apple"

orange = df[(df["product_name"].str.contains("Juice")) & (df["product_name"].str.contains("Orange")) & df["categories_en"].str.contains("Fruit-based beverages")].copy()
orange["clss"] = "Orange"

cola = df[df["categories_en"].str.contains("Colas")].copy()
cola["clss"] = "Cola"

juices = pd.concat([apple, orange, cola])
filtered = juices.dropna(axis=1, how='all').dropna(axis = 1, thresh = 500)
data = filtered[["product_name", "brands", "countries", "energy_100g", "fat_100g", "carbohydrates_100g", "sugars_100g", "proteins_100g", "clss"]]
data = data[data["energy_100g"].notnull() & data["sugars_100g"].notnull() & data["carbohydrates_100g"].notnull() & data["fat_100g"].notnull() & data["proteins_100g"].notnull()]


data.to_csv("./foods.csv", index = False)


# In[ ]:





# In[ ]:





