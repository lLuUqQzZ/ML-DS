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

# Datenquelle: https://www.kaggle.com/snap/amazon-fine-food-reviews
# 
# Davon betrachten wir nur die ersten 10.000 Zeilen.

# In[1]:


import pandas as pd

df = pd.read_csv("./Reviews_10000.csv.bz2")
df.head()


# In[2]:


texts = df["Text"]


# In[3]:


import nltk

texts_transformed = []
for review in texts: 
    sentences = nltk.sent_tokenize(review)
    adjectives = []
    
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words_tagged = nltk.pos_tag(words)
        
        for word_tagged in words_tagged:
            if word_tagged[1] == "JJ":
                adjectives.append(word_tagged[0])
                
    texts_transformed.append(" ".join(adjectives))


# In[4]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


# In[5]:


X = texts_transformed
y = df["Score"] >= 4


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

cv = CountVectorizer(max_features = 50)
cv.fit(X_train)

X_train = cv.transform(X_train)
X_test = cv.transform(X_test)


# In[16]:


model = MultinomialNB()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[ ]:





