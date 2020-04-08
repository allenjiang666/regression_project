from acquire import acquire_data
import pandas as pd
import numpy as np 

def prep_data():
    # acquire data
    df = acquire_data()
    # drop rows with missing values
    df.dropna(inplace = True)
    # drop row with 0 bathroom
    df = df[df.bathroomcnt != 0]

    # drop outliers from home_size
    home_size_percentile = df.home_size.quantile(.99)
    df = df[df.home_size <= home_size_percentile]
    # drop outliers from bedroom count
    bedroom_percentitle = df.bedroomcnt.quantile(.99)
    df = df[df.bedroomcnt <= bedroom_percentitle]
    # drop outliers from bathroom cnt
    bathroom_percentile = df.bathroomcnt.quantile(.99)
    df = df[df.bathroomcnt <= bathroom_percentile]
    # drop outliers from home values
    homevalue_percentile = df.home_value.quantile(.99)
    df = df[df.home_value <= homevalue_percentile]
    return df