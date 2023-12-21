# Классификация изображений

from keras.layers import Dense
from keras.layers import Flatten
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

idxs = np.where((y_train == 0)|(y_train == 1))
y_train = y_train[idxs]
X_train = X_train[idxs]

idxs = np.where((y_test == 0)|(y_test == 1))
y_test = y_test[idxs]
X_test = X_test[idxs]


print(X_train.min(), X_train.max())

X_train = X_train/255
X_test = X_test/255

print(X_train.min(), X_train.max())

y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

X_train_resized = tf.image.resize(X_train[..., np.newaxis], (6,6))[...,0]
X_test_resized = tf.image.resize(X_test[..., np.newaxis], (6,6))[...,0]

X_train_resized[0].numpy().flatten()


tf.random.set_seed(9)

model = Sequential([
    Flatten(input_shape=(6,6)),
    Dense(2, activation='sigmoid')
])

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')
model.fit(X_train_resized, y_train_cat, epochs=5)

print('Предсказание нейронной сети: ')
pred = model.predict(X_test_resized[:1])
print(pred.argmax())
