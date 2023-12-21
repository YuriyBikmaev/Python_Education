import keras as k
import numpy as np
import tensorflow as tf

input_data = np.array([0.3, 0.7, 0.9])
output_data = np.array([0.5, 0.9, 1])

model = k.Sequential([k.Input(shape=(1,))])
model.add(k.layers.Dense(units = 1, activation = "linear"))
model.compile(loss="mse", optimizer="sgd")


fit_result = model.fit(x=input_data, y=output_data, epochs=100)

predicted = model.predict([0.5])
print(predicted)