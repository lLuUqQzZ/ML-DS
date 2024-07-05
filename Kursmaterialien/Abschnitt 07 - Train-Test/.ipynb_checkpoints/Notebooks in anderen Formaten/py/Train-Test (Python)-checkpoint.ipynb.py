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

# ## Train / Test in Python

# In[13]:


import pandas as pd

df = pd.read_csv("./wohnungspreise.csv")
df.head()


# In[35]:


from sklearn.model_selection import train_test_split

X = df[["Quadratmeter"]].values
Y = df[["Verkaufspreis"]].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0, test_size = 0.25)


# In[ ]:





# In[40]:


import matplotlib.pyplot as plt

plt.scatter(X_train, y_train)
plt.scatter(X_test, y_test, color = "red")
plt.show()


# In[41]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))


# In[43]:


import matplotlib.pyplot as plt

predicted = model.predict(X_test)

plt.scatter(X_test, y_test, color = "red")
plt.plot(X_test, predicted)
plt.show()


# In[ ]:





