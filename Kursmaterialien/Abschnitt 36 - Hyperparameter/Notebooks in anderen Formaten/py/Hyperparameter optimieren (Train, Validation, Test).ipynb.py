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


import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[17]:


from sklearn.model_selection import train_test_split

X = df[["age", "interest"]].values
y = df["success"].values

X_train, X_test, y_train, y_test = train_test_split(X, y)


# In[18]:


from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

# pipeline.set_params(knn__n_neighbors = 1)


# In[19]:


from sklearn.model_selection import GridSearchCV

clf = GridSearchCV(pipeline, param_grid = {
    "knn__n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})
clf.fit(X_train, y_train)

print(clf.best_params_)


# In[20]:


print(clf.score(X_test, y_test))


# In[21]:


print(clf.best_score_)


# In[ ]:





