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

# ## Lineare Regression (mit Bias)
# 
# #### Beispiel: Grad Celsius -> Fahrenheit

# In[5]:


X = [
    [-10],
    [0],
    [20]
]

y = [
    14,
    32,
    68
]


# In[8]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)


# In[10]:


print(model.coef_)
print(model.intercept_)


# In[ ]:


# X1 * 1.8 + 32


