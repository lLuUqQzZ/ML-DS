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

# ## Musterlösung: Um was für eine Pflanzenart handelt es sich?
# 
# Sage dazu die Spalte `Species` vorher.
# 
# Teile die Daten dazu zuerst in Trainings- und Testdaten auf. Skaliere anschließend die Daten auf ein einheitliches Maß, und vergleiche folgende Modelle:
# 
# - Logistische Regression
# - KNN

# In[15]:


import pandas as pd

df = pd.read_csv("./iris.csv")

df.head()


# In[22]:


from sklearn.model_selection import train_test_split

# Welche Spalten sollen zur Vorhersage verwendet werden
X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]].values

# Oder: Die Spalte "success" soll nicht zur Vorhersage verwendet werden:
# X = df.drop("success", axis = 1).values

y = df["Species"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = 0.25)


# In[23]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[24]:


from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[25]:


from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[26]:




# In[27]:


from sklearn.linear_model import LogisticRegression

model = LogisticRegression(multi_class = "multinomial", solver = "sag")
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[ ]:





# In[ ]:





