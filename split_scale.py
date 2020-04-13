import pandas as pd
import numpy as np
from prep import prep_data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def split_data():
    train, test = train_test_split(prep_data(), train_size = .8, random_state = 123)
    return train, test

def split_scale():
    train, test = train_test_split(prep_data(), train_size = .8, random_state = 123)
    scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)

    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])

    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])

    return train_scaled, test_scaled, scaler
    