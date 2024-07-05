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

# # Exkurs: Skimage

# In[29]:


from skimage import io, exposure

image = io.imread("./dragon.png")
io.imshow(image)


# In[33]:


image[:, :, :3].shape


# In[52]:


image_without_alpha = image[:, :, :3]
image_brighter = image_without_alpha + 40
# 0 - 255      230 + 40 = 15

image_brighter[image_brighter < image_without_alpha] = 255

io.imshow(image_brighter)


# In[ ]:





