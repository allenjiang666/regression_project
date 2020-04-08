import pandas as pd
from env import url

#Read from Zillow database and write df to a csv
query = '''
    SELECT calculatedfinishedsquarefeet as home_size, 
    bedroomcnt, bathroomcnt, taxvaluedollarcnt as home_value
    FROM properties_2017 
    JOIN predictions_2017 USING(id)
    WHERE transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30'
'''
df = pd.read_sql_query(query, url("zillow"))

# export a csv file
df.to_csv('zillow.csv')

# read first a few rows
df = pd.read_csv('zillow.csv',  index_col=0)
df.head()

# Summary stats
df.dtypes
df.shape
df.describe()

# Check null values 
df.isnull().sum()
df[df.home_size.isnull()]
df[df.home_value.isnull()]

