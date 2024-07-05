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

# In[1]:


import nltk


# ### POS Tagging
# 
# (http://www.nltk.org/book/ch05.html)

# In[43]:


text = "He went into a supermarket in St. Petersburg. There, he bought a better product for 9.99$. He knew it better"
sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence))
    
    final_sentence = []
    for tagged_word in tagged_words:
        final_sentence.append(tagged_word[0] + "/" + tagged_word[1])
        
    print(" ".join(final_sentence))


# In[ ]:





# In[12]:


nltk.help.upenn_tagset()


# In[ ]:





