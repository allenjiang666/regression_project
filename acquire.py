import pandas as pd
from env import url
import os.path

#Read from Zillow database and write df to a csv
def get_data_from_sql():
    query = '''
        SELECT calculatedfinishedsquarefeet as home_size, 
        bedroomcnt, bathroomcnt, taxvaluedollarcnt as home_value
        FROM properties_2017 
        JOIN predictions_2017 USING(id)
        WHERE transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30'
    '''
    df = pd.read_sql_query(query, url("zillow"))
    df.to_csv('zillow.csv')
    return df

#check if there is a csv file, if not run squl query
def acquire_data():
    if os.path.exists('zillow.csv'):
        df = pd.read_csv('zillow.csv',  index_col=0)
    else:
        df = get_data_from_sql()
    return df


