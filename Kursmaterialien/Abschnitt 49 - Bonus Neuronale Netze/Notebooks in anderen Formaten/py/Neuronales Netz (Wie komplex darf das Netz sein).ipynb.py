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

# In[5]:


# Vorstellung: MNIST-Daten!
# http://yann.lecun.com/exdb/mnist/
# FashionMNIST: https://github.com/zalandoresearch/fashion-mnist

import gzip
import numpy as np
from keras.utils import to_categorical

def open_images(filename):
    with gzip.open(filename, "rb") as file:
        data = file.read()
        return np.frombuffer(data, dtype=np.uint8, offset=16)            .reshape(-1, 28, 28)            .astype(np.float32)


def open_labels(filename):
    with gzip.open(filename, "rb") as file:
        data = file.read()
        return np.frombuffer(data, dtype=np.uint8, offset=8)
    
X_train = open_images("../data/fashion/train-images-idx3-ubyte.gz")
y_train = open_labels("../data/fashion/train-labels-idx1-ubyte.gz")

X_test = open_images("../data/fashion/t10k-images-idx3-ubyte.gz")
y_test = open_labels("../data/fashion/t10k-labels-idx1-ubyte.gz")

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


# ### Neuronales Netz (mit Softmax)

# In[2]:


from keras.models import Sequential
from keras.layers import Dense


# In[13]:


model = Sequential()

model.add(Dense(200, activation="sigmoid", input_shape=(784,)))
model.add(Dense(100, activation="sigmoid", input_shape=(784,)))
model.add(Dense(10, activation="softmax"))

# rmsprop, adam
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])


# In[14]:


model.fit(
    X_train.reshape(60000, 784),
    y_train,
    epochs=100,
    batch_size=1000)


# ### Es gilt: Das Netz passt sich an die Daten an.
# 
# - Testgenauigkeit nur minimal schlechter wie die Trainingsgenauigkeit: Das Modell darf vermutlich noch was komplexer sein 
# 
# - Testgenauigkeit sehr viel schlechter wie die Trainingsgenauigkeit: Das Modell ist zu komplex (das Modell hat sich zu stark an die Trainingsdaten angepasst)
# 
# - Beides schlecht: Du brauchst mehr Daten!

# In[15]:


model.evaluate(X_train.reshape(-1, 784), y_train)


# In[16]:


model.evaluate(X_test.reshape(-1, 784), y_test)


# In[ ]:





