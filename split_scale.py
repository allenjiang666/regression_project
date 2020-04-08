import pandas as pd
import numpy as np
from prep import prep_data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxSclaer

def split_data(df):
    train, test = train_test_split(df, train_size = .8, random_state = 123)
    return train, test

def scale_data(df):
    return
    