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

# # Übung: Reguläre Ausdrücke
# 
# **Aufgabe:** Extrahiere die Datumsangaben mit Hilfe von regulären Ausdrücken.
# 
# **Tipp:** Du darfst hierzu mehrere reguläre Ausdrücke verwenden, also beispielsweise:
# 
# ```python
# import re
# 
# re1 = re.compile("") # Regulärer Ausdruck für 01.05.2018 (Tag, Monat, Jahr)
# re2 = re.compile("") # Regulärer Ausdruck für 2018/14/05 (Jahr / Tag / Monat)
# re3 = re.compile("") # Regulärer Ausdruck für 05/2018 (Monat / Jahr)
# 
# ```
# 
# Gehe also alle `sentences` durch, und extrahiere die Datumsangabe aus dem String. Du brauchst die Datumswerte nicht umzuwandeln.

# In[11]:


import re

p = re.compile("a[0-9]{2}a")

print(p.search("Hallo a123a a12a"))


# In[6]:


sentences = [
    "Am 05.06.2018 findet ein cooles Event statt",
    "Please follow our invitation and visit us on 2018/14/05",
    "Im Monat 05/2018 ist oft gutes Wetter",
    "Der Lottogewinn war 10.000.000€ groß. Er wurde am 04.06.2018 ausgeschüttet",
    "Im Monat 01/2018 war in Sofia heftiger Smog",
    "Dein Flug in den Urlaub geht am 06.07.2018",
]


# **Gewünschte Ausgabe:**
# 
# ```
# 05.06.2018
# 2018/14/05
# 05/2018
# 04.06.2018
# 01/2018
# 06.07.2018
# ```

# **Bonusaufgabe:** Wandel zudem auch alle Datumsangaben in ein einheitliches Format um. Wenn nur ein Monat angegeben ist, setze den Tag auf den Monatsersten. 
# 
# **Bonusaufgabe - Schwere Lösung:** Schau dir dazu auf jeden Fall das Datetime-Modul an (`from datetime import datetime`), und dazu die `strptime` - Funktion. Damit kannst du einen Datumswert nach Python einlesen (https://docs.python.org/3/library/datetime.html). Hierzu solltest du dir dann auch die `strftime` - Funktion anschauen. 
# 
# Idee wäre hier also: Du liest das Datum über `strptime` ein, dann hast du ein Python-Datums-Objekt, und dieses wandelst du dann über `strftime` wieder zurück in das deutsche Datumsformat um. Vorteil davon ist, dass du Python-Datums-Objekte gut weiterverarbeiten kannst - Nachteil, dass diese Lösung etwas aufwendiger ist.
# 
# **Bonusaufgabe - Einfachere Lösung:** Alternativ kannst du auchb einfach nur mit einem `"2018/14/05".split("/")`, etc. arbeiten, die Liste dann verändern, und zum Beispiel mit einem `".".join(liste)` wieder zusammenführen - das geht auch. 
# 
# **Bonusaufgabe - gewünschte Ausgabe:**
# 
# ```
# 05.06.2018
# 14.05.2018
# 01.05.2017
# 04.06.2018
# 01.01.2018
# 06.07.2018
# ```

# In[ ]:





