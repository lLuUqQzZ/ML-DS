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

# # Farben komprimieren mit KMeans

# In[6]:


from skimage import io, exposure
import numpy as np

image = io.imread("./dragon.png")[:, :, :3]
io.imshow(image)


# In[7]:


image_reshaped = image.reshape(-1, 3)


# In[8]:


image_reshaped[0]


# In[9]:


from sklearn.cluster import KMeans

model = KMeans(n_clusters = 32, n_init = 1)
model.fit(image_reshaped)


# In[55]:


colors = model.cluster_centers_.astype("uint8")
pixels = model.labels_

np.savez_compressed("./image.npz", pixels = pixels, colors = colors)

with np.load("./image.npz") as file:
    pixels = file["pixels"]
    colors = file["colors"]

pixels_transformed = []
for pixel in pixels:
    pixels_transformed.append(colors[pixel])


# In[56]:


pixels_transformed = np.array(pixels_transformed)


# In[57]:


image_restored = np.array(pixels_transformed).reshape(900, 1200, 3)


# In[58]:


io.imshow(image_restored)


# In[ ]:





# In[ ]:





