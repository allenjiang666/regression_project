import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

from split_scale import split_scale
from feature_selection import rfe, k_best

import warnings
warnings.filterwarnings("ignore")

def model():
    train, test, scaler= split_scale()
    train, selector = rfe(train, 3)
    X = train.drop(columns = 'home_value')
    y = train[['home_value']]
    lm2 = LinearRegression()
    lm2.fit(X, y)
    predictions = pd.DataFrame({'actual': train.home_value})
    predictions['predicted'] = lm2.predict(X)
    RMSE_lm2 = np.sqrt(mean_squared_error(predictions.actual, predictions.predicted))
    rfe_r2 = lm2.score(X, y)
    print("RMSE", RMSE_lm2, "R2", rfe_r2)
    