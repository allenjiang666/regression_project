import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

from split_scale import split_scale


def k_best(train, k):
    X = train.drop(columns = 'home_value')
    y = train[['home_value']]
    f_selector = SelectKBest(f_regression, k)
    f_selector.fit(X,y)
    X_reduced = f_selector.transform(X)
    f_support = f_selector.get_support()
    feature_eleminated = X.loc[:,~f_support].columns
    df = train.drop(columns = feature_eleminated)
    return df, f_selector

def rfe(train, k):
    X = train.drop(columns = 'home_value')
    y = train[['home_value']]
    lm = LinearRegression()
    rfe = RFE(lm, k)
    X_rfe = rfe.fit_transform(X,y)
    feature_selected = X.loc[:,rfe.support_].columns
    feature_eleminated = X.loc[:,~rfe.support_].columns.tolist()
    df = train.drop(columns = feature_eleminated)
    return df, rfe