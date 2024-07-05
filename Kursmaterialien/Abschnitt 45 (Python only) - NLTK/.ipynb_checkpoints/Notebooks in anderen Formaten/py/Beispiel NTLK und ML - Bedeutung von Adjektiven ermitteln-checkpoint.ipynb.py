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

# In[2]:


import pandas as pd

df = pd.read_csv("./Reviews_10000.csv.bz2")
df.head()


# In[3]:


texts = df["Text"]


# In[14]:


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


# In[16]:


texts_transformed


# In[ ]:





