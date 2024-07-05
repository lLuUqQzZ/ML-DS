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

# ## Aufgabe: Um was für eine Pflanzenart handelt es sich?
# 
# Sage dazu die Spalte `Species` vorher.
# 
# Teile die Daten dazu zuerst in Trainings- und Testdaten auf. Skaliere anschließend die Daten auf ein einheitliches Maß, und vergleiche folgende Modelle:
# 
# - Logistische Regression
# - KNN (probiere hier verschiedene Werte für `k` aus, z.B. k = 1, k = 3, k = 5). Bitte beachte: Dieser Parameter heißt in sklearn `n_neighbors`!
# 
# #### Hinweise: 
#   - Die Spalte `Id` wird für das Modell nicht benötigt, diese Spalte
#     sollte also auf keinen Fall in die Berechnung vom Modell mit
#     einfließen.
#   - Du möchtest hier die Spalte `Species` vorhersagen. Diese enthält
#     drei verschiedene Werte - Sklearn kommt damit automatisch klar! :)

# In[1]:


import pandas as pd

df = pd.read_csv("./iris.csv")

df.head()


# In[ ]:





# In[ ]:





