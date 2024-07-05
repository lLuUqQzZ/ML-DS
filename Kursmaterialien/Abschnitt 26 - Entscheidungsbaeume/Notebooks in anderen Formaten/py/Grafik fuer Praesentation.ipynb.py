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

# In[12]:



import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)

sns.set_style("whitegrid", {"axes.facecolor": "#00000000", "figure.facecolor": "#00000000"})
sns.set_context("notebook", font_scale=1.5)

plt.plot(x, -x * np.log2(x) - (1 - x) * np.log2(1 - x), linewidth = 3)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Wahrscheinlichkeit (p)")
plt.ylabel("Entropie (H)")
plt.show()


# In[1]:


import numpy as np


# In[ ]:





