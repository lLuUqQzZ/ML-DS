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

# In[3]:


import pandas as pd

# Daten von: https://www.kaggle.com/uciml/sms-spam-collection-dataset
# Aufbereitet wie folgt:
#  - 2 "Unnamed" Spalten entfernt
#  - Kodierung auf utf-8 geändert
#  - Spalten unbenannt

df = pd.read_csv("./spam.csv")

df.head()


# In[23]:


print(len(df))


# In[45]:


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

X = df["message"]
y = df["type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

cv = CountVectorizer(min_df = 0.01, max_df = 0.1)
cv.fit(X_train)

X_train = cv.transform(X_train)
X_test = cv.transform(X_test)


# In[46]:


print(X_train.shape)


# In[ ]:





# In[48]:


from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[ ]:





