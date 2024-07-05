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

# ## Lineare Regression
# 
# #### Beispiel: Kilometer in Meilen umrechnen

# In[19]:


X = [
    [10],
    [15],
    [60]
]

y = [
    6.2,
    9.3,
    37.3
]


# In[20]:


from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept = False)
model.fit(X, y)


# In[21]:


model.coef_


# In[22]:


print(120 * 0.62152866)


# In[23]:


model.predict([
    [120],
    [130]
])


# In[ ]:





# In[ ]:





