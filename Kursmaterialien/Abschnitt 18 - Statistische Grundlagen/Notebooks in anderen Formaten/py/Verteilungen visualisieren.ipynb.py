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

# In[26]:


import numpy as np

levels = np.random.normal(300, 10, 10000)
print(levels)


# In[30]:



import matplotlib.pyplot as plt

plt.hist(levels, bins = 100)
plt.xlim(100, 500)
plt.show()


# In[29]:


import numpy as np

levels2 = np.random.normal(300, 50, 10000)


import matplotlib.pyplot as plt

plt.hist(levels2, bins = 100)
plt.xlim(100, 500)
plt.show()


# In[ ]:





