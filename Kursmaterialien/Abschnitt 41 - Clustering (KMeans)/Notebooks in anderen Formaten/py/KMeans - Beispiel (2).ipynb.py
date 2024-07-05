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

# # KMeans - Clustering am Beispiel (echte Daten!)
# 
# Wir werden in dieser Lektion die Daten nach folgenden Spalten clustern:
# 
# - `yearOfRegistration`
# - `price`

# In[1]:


import pandas as pd

df = pd.read_csv("./autos_prepared.csv")

df.head()


# In[2]:



import matplotlib.pyplot as plt

plt.scatter(df["yearOfRegistration"], df["price"])
plt.show()


# In[3]:


X = df[["yearOfRegistration", "price"]]


# In[4]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)


# In[43]:


from sklearn.cluster import KMeans

model = KMeans(n_clusters = 3)
model.fit(X_transformed)

labels = model.labels_
centers = model.cluster_centers_

centers_transformed = scaler.inverse_transform(centers)


# In[44]:



import matplotlib.pyplot as plt

plt.scatter(df["yearOfRegistration"], df["price"], c = labels, alpha = 0.4, s = 10)

plt.scatter(
    centers_transformed[:, 0], 
    centers_transformed[:, 1], 
    c = range(len(centers_transformed)), 
    marker = "X", 
    s = 150)

plt.show()


# In[ ]:





# In[36]:





# In[ ]:





