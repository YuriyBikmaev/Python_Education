# Умножение входных данных на 3


from keras.layers import Dense
from keras.models import Sequential
import tensorflow as tf
import numpy as np
import pandas as pd

#tf.random.set_seed(1)

model = Sequential([
    Dense(1, input_shape=(1,), activation='linear')
])

#model.summary()
#создание обучающих данных
X = np.array([[1],[3],[2],[10],[4],[7],[8]])
y = np.array([[3,9,6,30,12,21,24]]).T

w1, w0 = model.get_weights()
print(f'w1 = {w1}, w0 = {w0}')

model.compile(optimizer='sgd', loss='mse', metrics='mae')
model.fit(X, y, epochs=100)

inp1, inp2 = 5, -9
print(f'Проверка новых данных: {inp1}, {inp2}')
print(f'Предсказание нейронной сети:')
result = model.predict(np.array([[inp1],[inp2]]))
print(result)

w1, w0 = model.get_weights()
print(f'w1 = {w1}, w0 = {w0}')

print(pd.DataFrame({
    'true': np.squeeze(y),
    'pred': np.squeeze(model.predict(X))
}))
