import keras as k
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("AI\\titanic.csv")
input_names = ["Age", "Sex", "Pclass"]
output_names = ["Survived"]

max_age = 100
encoders = {"Age": lambda age: [age/max_age],
            "Sex": lambda gen: {"male": [0], "female": [1]}.get(gen),
            "Pclass": lambda pclass: {1: [1,0,0], 2: [0,1,0], 3:[0,0,1]}.get(pclass),
            "Survived": lambda s_value: [s_value]}

def dataframe_to_dict(df):
    result = dict()
    for column in df.columns:
        values = data_frame[column]
        result[column] = values
    return result

def make_supervised(df):
    raw_input_data = data_frame[input_names]
    raw_output_data = data_frame[output_names]
    return {"inputs": dataframe_to_dict(raw_input_data),
            "outputs": dataframe_to_dict(raw_output_data)}

def encode(data):
    vectors = []
    for data_name, data_values in data.items():
        encoded = list(map(encoders[data_name], data_values))
        vectors.append(encoded)
    formatted = []
    for vector_raw in list(zip(*vectors)):
        vector = []
        for el in vector_raw:
            for e in el:
                vector.append(e)
        formatted.append(vector)
    return formatted

supervised = make_supervised(data_frame)
encoded_inputs = np.array(encode(supervised["inputs"]))
encoded_outputs = np.array(encode(supervised["outputs"]))


train_x = encoded_inputs[:800]
train_y = encoded_outputs[:800]

test_x = encoded_inputs[870:]

model = k.Sequential()
model.add(k.layers.Dense(units=5, activation="relu"))
model.add(k.layers.Dense(units=1, activation="sigmoid"))
model.compile(loss="mse", optimizer="sgd", metrics=["accuracy"])
# model.built = True
# model.load_weights("AI\weight.h5")
#fit_result = model.fit(x=train_x, y=train_y, epochs=1000, validation_split=0.2)
#model.built = True
model.load_weights('AI\weigth')

# plt.title("Losses train/validation")
# plt.plot(fit_result.history["loss"], label="Train")
# plt.plot(fit_result.history["val_loss"], label="Validation")
# plt.legend()
# plt.show()

# plt.title("Accuracies train/validation")
# plt.plot(fit_result.history["accuracy"], label="Train")
# plt.plot(fit_result.history["val_accuracy"], label="Validation")
# plt.legend()
# plt.show()



predicted_test = model.predict(test_x)
real_data = data_frame.iloc[870:][input_names]
real_data["PSurvived"] = predicted_test
print(real_data)

#model.save('model100')
#model.save_weights('AI\weigth')
