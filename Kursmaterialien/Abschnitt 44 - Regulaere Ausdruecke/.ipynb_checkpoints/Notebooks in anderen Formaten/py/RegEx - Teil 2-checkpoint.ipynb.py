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

# # Reguläre Ausdrücke - Teil 2

# In[9]:


import re

p = re.compile(" [0-9]+ ")

print(p.findall("Für 1 Knusperbrötchen habe ich 1.99€ bezahlt"))
print(p.findall("Für 12 Knusperbrötchen habe ich 1,99$ bezahlt"))
print(p.findall("Für 123 Knusperbrötchen habe ich 10.99€ bezahlt"))


# In[15]:


import re

p = re.compile(" [0-9]+[\.,][0-9]{2}[$€]? ")

print(p.findall("Für 1 Knusperbrötchen habe ich 1.99€ bezahlt"))
print(p.findall("Für 12 Knusperbrötchen habe ich 1,99$ bezahlt"))
print(p.findall("Für 123 Knusperbrötchen habe ich 10.99 bezahlt"))


# In[ ]:





