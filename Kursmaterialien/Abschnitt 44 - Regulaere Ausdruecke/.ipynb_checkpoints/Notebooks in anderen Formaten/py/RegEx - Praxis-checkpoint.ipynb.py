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

# # Reguläre Ausdrücke - Beispiel: E-Mail-Adressen finden

# In[23]:


import re

p = re.compile("[a-zA-Z0-9\+]+@[a-zA-Z0-9]+\.[\.a-zA-Z0-9]+")

sentences = [
    "Meine E-Mail-Adresse ist hallo+welt@codingcourses.tv",
    "Bitte keine E-Mails an info@codingcourses.tv senden",
    "Saturday@ Hotel XYZ findet ein Event statt. Zur Teilnahme kannst du eine E-Mail an veranstaltung@codingcourses.tv schicken"
]

for sentence in sentences:
    print(p.search(sentence))


# In[33]:


import re

p = re.compile("[a-zA-Z0-9\+]+@[a-zA-Z0-9]+\.[\.a-zA-Z0-9]+")

sentences = [
    "Hallo Welt",
    "Meine E-Mail-Adresse ist hallo+welt@codingcourses.tv",
    "Bitte keine E-Mails an info@codingcourses.tv senden",
    "Saturday@ Hotel XYZ findet ein Event statt. Zur Teilnahme kannst du eine E-Mail an veranstaltung@codingcourses.tv schicken"
]

for sentence in sentences:
    match = p.search(sentence)
    if match:
        print(match[0])


# In[ ]:





