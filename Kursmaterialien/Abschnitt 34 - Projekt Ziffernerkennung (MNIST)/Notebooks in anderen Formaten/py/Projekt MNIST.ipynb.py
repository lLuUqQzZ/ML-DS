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


import gzip
import os
import numpy as np

train_data = os.path.join("..", "data", "mnist", "train-images-idx3-ubyte.gz")
train_labels = os.path.join("..", "data", "mnist", "train-labels-idx1-ubyte.gz")

test_data = os.path.join("..", "data", "mnist", "t10k-images-idx3-ubyte.gz")
test_labels = os.path.join("..", "data", "mnist", "t10k-labels-idx1-ubyte.gz")


# In[2]:


def mnist_images(filename):
    with gzip.open(filename, "rb") as file:
        data = np.frombuffer(file.read(), np.uint8, offset = 16)
        return data.reshape(-1, 28, 28) / 255
    
def mnist_labels(filename):
    with gzip.open(filename, "rb") as file:
        return np.frombuffer(file.read(), np.uint8, offset = 8)

X_train = mnist_images(train_data)
y_train = mnist_labels(train_labels)

X_test = mnist_images(test_data)
y_test = mnist_labels(test_labels)


# In[3]:



import matplotlib.pyplot as plt

print(y_train[25])
plt.imshow(X_train[25])
plt.show()


# In[ ]:





# In[6]:


from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver = "saga", n_jobs = 4)
model.fit(X_train.reshape(-1, 784), y_train)


# In[8]:


model.score(X_test.reshape(-1, 784), y_test)


# In[ ]:





