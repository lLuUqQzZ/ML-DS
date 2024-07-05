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

# ## Aufgabe: Hyperparamter optimieren
# 
# Aufgabe: Finde gute Hyperparemter (`C` und `gamma`) für eine SVM (sklearn.svm.SVC).
# 
# In der Musterlösung werden wir hier folgende Werte für `C` bzw. `gamma` durchprobieren:
# 
# - **C:** 0.001, 0.01, 0.1, 1, 10
# - **gamma:** 0.001, 0.01, 0.1, 1, 10
# 
# **Wichtig:** Der Parameter `random_state` bei der `train_test_split` - Funktion muss auf `0` gesetzt sein - sonst werden u.U. andere Werte herauskommen!

# In[1]:


import pandas as pd

df = pd.read_csv("./classification.csv")

df.head()


# In[2]:


from sklearn.model_selection import train_test_split

X = df[["age", "interest"]].values
y = df["success"].values

X_train, X_validation, y_train, y_validation = train_test_split(X, y, random_state = 0)


# In[3]:


from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC())
])


# In[6]:


from sklearn.model_selection import GridSearchCV

clf = GridSearchCV(pipeline, param_grid = {
    "svm__C": [0.001, 0.01, 0.1, 1, 10],
    "svm__gamma": [0.001, 0.01, 0.1, 1, 10]
})
clf.fit(X_train, y_train)

print(clf.best_params_)


# In[7]:


print(clf.score(X_validation, y_validation))


# In[ ]:





# In[ ]:





