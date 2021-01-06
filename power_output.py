import tensorflow.keras as kr
# Numerical arrays
import numpy as np
# Data frames.
import pandas as pd
# Plotting
import matplotlib.pyplot as plt
# neural neworks
import tensorflow.keras as kr

def load_model():
    data = pd.read_csv('power_production.csv')
    # drop rows where the power putput is zero even though wind speed > 10
    # https://stackoverflow.com/questions/52456874/drop-rows-on-multiple-conditions-in-pandas-dataframe   
    df_new = data.drop(data[(data['speed'] > 10.0) & (data['power'] == 0.0)].index)  
    train = pd.DataFrame()
    msk = np.random.rand(len(df_new)) < 0.8
    train = df_new[msk]
    test = df_new[~msk]
    train_x = train.iloc[:,0]
    train_y = train.iloc[:,1]
    test_x = test.iloc[:,0]
    test_y = test.iloc[:,1]

    # Train a model.
    m = kr.models.Sequential()
    m.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
    m.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
    m.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')
    m.fit(train_x, train_y, epochs=500, batch_size=10)
    # power_out = m.predict([wind_speed])
    return m


# save the model
# https://machinelearningmastery.com/save-load-keras-deep-learning-models/#:~:text=Keras%20separates%20the%20concerns%20of,different%20formats%3A%20JSON%20and%20YAML.
m = load_model()
m.save("model.h5")


