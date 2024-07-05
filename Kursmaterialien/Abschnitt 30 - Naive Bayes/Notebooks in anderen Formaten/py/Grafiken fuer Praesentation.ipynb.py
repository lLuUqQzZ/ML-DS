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

# In[92]:



import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


n_cats = 6
n_dogs = 12

x_cats = np.random.normal(25, 10, n_cats)
y_cats = np.random.normal(10, 2, n_cats)

x_dogs = np.random.normal(35, 5, n_dogs)
y_dogs = np.random.normal(30, 10, n_dogs)

x = np.append(x_cats, x_dogs)
y = np.append(y_cats, y_dogs)
z = np.append([0] * n_cats, [1] * n_dogs)


# In[93]:


sns.set_style("whitegrid", {"axes.facecolor": "#00000000", "figure.facecolor": "#00000000"})
sns.set_context("notebook", font_scale=1.5)

g = sns.JointGrid(x_cats, y_cats, xlim = (0, 100), ylim = (0, 50))
g = g.plot_joint(plt.scatter, color="green", edgecolor="white", marker = "X", s = 200)
g = g.plot_marginals(sns.distplot, kde=False, color="green")
g


# In[94]:


sns.set_style("whitegrid", {"axes.facecolor": "#00000000", "figure.facecolor": "#00000000"})
sns.set_context("notebook", font_scale=1.5)

g = sns.JointGrid(x_dogs, y_dogs, xlim = (0, 100), ylim = (0, 50))
g = g.plot_joint(plt.scatter, color="blue", edgecolor="white", marker = "X", s = 200)
g = g.plot_marginals(sns.distplot, kde=False, color="blue")
g


# In[ ]:





# In[ ]:





