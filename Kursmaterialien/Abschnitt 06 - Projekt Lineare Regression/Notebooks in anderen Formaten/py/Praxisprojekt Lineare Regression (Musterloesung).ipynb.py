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

# ### Praxisprojekt: Lineare Regression

# In[5]:


import pandas as pd

df = pd.read_csv("./autos_prepared.csv")


# In[6]:


df.head()


# ## Teil 1: Scatter-Plot zeichnen

# In[7]:


import matplotlib.pyplot as plt

plt.scatter(df["kilometer"], df["price"])
plt.show()


# ## Teil 2: Lineare Regression ausführen

# In[8]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[["kilometer"]], df[["price"]])

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))

# 15988.72674252 - 0.0879714 * [Anzahl km] 


# ### Teil 3: Werte für unsere Linie vorhersagen

# In[15]:


predicted = model.predict([[0], [130000]])
print(predicted)


# ### Teil 4: Linie in Grafik einzeichnen

# In[14]:


import matplotlib.pyplot as plt

plt.scatter(df["kilometer"], df["price"])
plt.plot([0, 130000], predicted, color="red")
plt.show()


# ### Teil 5: Vorhersage für 50.000km machen

# In[12]:


model.predict([[50000]])


