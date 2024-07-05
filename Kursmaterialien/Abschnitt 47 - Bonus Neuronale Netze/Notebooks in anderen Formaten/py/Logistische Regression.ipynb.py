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

# ## Logistische Regression
# 
# Ein einfaches Beispiel: Wird ein Studierender die Prüfung bestehen?

# In[109]:


# X = Wie viele Stunden hat er gelernt?

X = [
    [50],
    [60],
    [70],
    [20],
    [10],
    [30],
]

y = [
    1, 
    1,
    1,
    0, 
    0, 
    0,
]


# In[110]:


from sklearn.linear_model import LogisticRegression

model = LogisticRegression(C = 100000)
model.fit(X, y)


# In[112]:


model.predict([
    [44]
])


# In[114]:


model.predict_proba([
    [35]
])


# In[ ]:





