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

df = pd.read_csv("./sf_salaries.csv", low_memory = False)

df.head()


# In[7]:


year_2011 = df[df["Year"] == 2011]
year_2011["TotalPay"].mean()


# In[8]:


year_2012 = df[df["Year"] == 2012]
year_2012["TotalPay"].mean()


# In[9]:


year_2013 = df[df["Year"] == 2013]
year_2013["TotalPay"].mean()


# In[10]:


year_2014 = df[df["Year"] == 2014]
year_2014["TotalPay"].mean()


# In[11]:


df["TotalPay"].mean()


# In[12]:


df["TotalPay"].median()


# In[15]:


import matplotlib.pyplot as plt

plt.hist(df["TotalPay"], bins = 100)
plt.show()


# In[ ]:





