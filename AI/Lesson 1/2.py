# Сложение двух чисел посытупаемых на вход


from keras.layers import Dense
from keras.models import Sequential
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

X1 = np.random.randint(1, 10, size=50)
X2 = np.random.randint(1, 10, size=50)

y = X1 + X2

X = np.vstack([X1, X2]).T
print(X)

y = y[None]
y = y.T
print(y)


# делаем нормализацию данных
mms = MinMaxScaler()
X_norm = mms.fit_transform(X)
print(X_norm)

tf.random.set_seed(9)

model = Sequential([
    Dense(3, input_shape = (2,), activation='linear'),
    Dense(1, activation='linear')
])

model.compile(optimizer='sgd', loss='mse', metrics='mae')
model.fit(X_norm, y, epochs=200)

test_X = [[4, 2],
          [6, 2]]
test_X = mms.transform(test_X)
print('Предсказание нейроной сети:')
print(model.predict(np.array(test_X)))

result = pd.DataFrame({
    'x1': X[:,0],
    'x2': X[:,1],
    'true': np.squeeze(y),
    'pred': np.squeeze(model.predict(X_norm))
})
print(result)
