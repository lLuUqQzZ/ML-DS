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



import moviepy


# In[2]:


from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=200, n_features=2, cluster_std=1.25, centers=[(-5, -5), (0, 0), (5, 5)], shuffle=False, random_state=0)


# In[3]:



import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1])
plt.show()


# In[5]:


from sklearn.cluster import KMeans


# In[27]:


from moviepy.editor import VideoClip
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage


n_clusters = 3

def make_figure(t):
    fig = Figure(dpi = 1600)
    canvas = FigureCanvas(fig)
    ax = fig.gca()

    if t == 0:
        ax.scatter(X[:, 0], X[:, 1], alpha = 0.3)
        ax.set_title("KMeans (Vorher)")
    else:
        ax.set_title("KMeans (Schritt #" + str(int(t)) + ")")
        model = KMeans(n_clusters=n_clusters, random_state = 44, max_iter=t, n_init = 1, init = "random")
        model.fit(X)
        
        for label in range(0, n_clusters):
            color = plt.cm.Dark2(label)
            print(color)
            
            ax.scatter(
                model.cluster_centers_[label, 0], 
                model.cluster_centers_[label, 1], 
                marker = "X", 
                s = 100,
                color = color
            )
            
            ax.scatter(
                X[model.labels_ == label, 0], 
                X[model.labels_ == label, 1], 
                color = color,
                alpha = 0.5
            )
    return fig

def make_frame(t):
    fig = make_figure(t)
    return mplfig_to_npimage(fig)

animation = VideoClip(make_frame, duration=7).resize(0.125)
animation.ipython_display("m.gif", fps=1, loop=True, autoplay=True, width=500)


# In[28]:


animation.write_gif("kmeans.gif", fps = 1)


# In[33]:


from sklearn.metrics import silhouette_score

clusters = range(2, 10)
scores = []

for i in clusters:
    model = KMeans(n_clusters=i)
    model.fit(X)
    
    print(silhouette_score(X, model.labels_, metric='euclidean'))
    scores.append(model.score(X))
    
import matplotlib.pyplot as plt

plt.plot(clusters, scores)


# In[ ]:





