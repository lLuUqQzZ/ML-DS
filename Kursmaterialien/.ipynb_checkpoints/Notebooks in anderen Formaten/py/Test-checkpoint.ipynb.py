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

# In[ ]:


Hallo Welt


# In[139]:




# In[207]:


from sklearn.datasets import make_classification

points, y = make_classification(300, 2, n_informative = 2, n_redundant = 0, flip_y = 0.05, hypercube = True, n_clusters_per_class = 2)


import matplotlib.pyplot as plt

plt.scatter(points[:, 0], points[:, 1], c = y)
plt.show()
print(y)


# In[ ]:





# In[208]:


import pandas as pd

df = pd.DataFrame({"interview": points[:, 1], "education": points[:, 0], "success": y})

df["success"] = (df["education"] > 1.5) | df["success"]

df = df.append({"interview": -0.5, "education": 3, "success": 0}, ignore_index = True)

df = df.append({"interview": -0.75, "education": 3.5, "success": 0}, ignore_index = True)

df = df.append({"interview": -1, "education": -1, "success": 1}, ignore_index = True)

df["education"] = (df["education"] + 2) * 1.75

df["interview"] = (df["interview"] + 2.5) * 19


print(df.shape)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,7))
plt.scatter(df["education"], df["interview"], c = df["success"])
plt.show()


# In[116]:


df.to_csv("./classification.csv", index = False)


# In[49]:


df = pd.read_csv("./classification.csv")

import numpy as np

xmesh = np.linspace(min(df["education"]), max(df["education"]), 1000)
ymesh = np.linspace(min(df["interview"]), max(df["interview"]), 1000)
xv, yv = np.meshgrid(xmesh, ymesh)


# In[55]:


from sklearn.svm import SVC

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


model = SVC(probability = True, C = 0.2)
# model = KNeighborsClassifier(n_neighbors = 10)
model.fit(df[["education", "interview"]].values, df["success"].values)

print(model.score(df[["education", "interview"]].values, df["success"].values))


Z = model.predict_proba(np.c_[xv.ravel(), yv.ravel()])[:, 1]
Z = Z.reshape(xv.shape)

# plt.imshow(Z, extent=(min(xmesh), max(xmesh), min(ymesh), max(ymesh)), origin='lower', alpha = 0.7)
plt.contourf(xmesh, ymesh, Z, alpha = 0.8)
plt.scatter(df["education"], df["interview"], c = df["success"])
plt.show()


# In[53]:




# In[13]:


gdp_2016 = [["123" , 18.6], [123 , 11.2], [123 , 4.94], [123, 3.46]]
np.array(gdp_2016)[:, 1].astype(float).sum()


# In[ ]:





