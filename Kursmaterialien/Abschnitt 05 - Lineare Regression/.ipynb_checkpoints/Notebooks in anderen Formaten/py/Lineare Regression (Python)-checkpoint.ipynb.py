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

# In[30]:


import pandas as pd

df = pd.read_csv("./wohnungspreise.csv")


# In[31]:


df.head()


# In[ ]:





# In[37]:


import matplotlib.pyplot as plt

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.show()


# In[ ]:





# In[40]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[["Quadratmeter"]], df[["Verkaufspreis"]])

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))


# In[ ]:


# Verkaufspreis = 3143.28481869 + 5071.35242619 * Quadratmeter
# y = 3143.28481869 + 5071.35242619 * x


# In[42]:


print(3143.28481869 + 5071.35242619 * 40)


# In[84]:


min_x = min(df["Quadratmeter"])
max_x = max(df["Quadratmeter"])

predicted = model.predict([[min_x], [max_x]])


# In[87]:


plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.plot([min_x, max_x], predicted, color = "red")
plt.show()


