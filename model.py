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
   
    
    #plot residuals
    residuals = predictions.actual - predictions.predicted
    plt.hlines(0, predictions.actual.min(), predictions.actual.max(), ls=':')
    plt.scatter(predictions.actual, residuals)
    plt.ylabel('residual ($y - \hat{y}$)')
    plt.xlabel('actual value ($y$)')
    plt.title('Actual vs Residual')
    
    #X_test = test.drop(columns = 'home_value')
    y_test = test[['home_value']]
    X_test_rfe = selector.transform(X_test)
    y_test_predictions = lm2.predict(X_test_rfe)
    RMSE_lm2_t = np.sqrt(mean_squared_error(y_test, y_test_predictions))
    
    print("RMSE", RMSE_lm2, "R2", rfe_r2, "Test_RMSE", RMSE_lm2_t)
    