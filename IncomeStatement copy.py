import intrinio
import json
import pandas as pd
import csv
import ijson
import requests


intrinio.username = 'YOUR USERNAME'
intrinio.password = 'YOUR PASSWORD'
base_url = 'https://api.intrinio.com'


ticker = 'ISSC'
request_url = base_url + '/financials/standardized'
query_params = {
    'ticker': ticker,
    'statement': 'income_statement',
    'type': 'TTM'
}

response = requests.get(request_url, params=query_params, auth=(intrinio.username, intrinio.password))
if response.status_code == 401: print('Unauthroized'); exit()

data = response.json()['data']

for row in data:
    tag = row['tag']
    value = row['value']
    print(tag + ': ' +str(value))

df = pd.DataFrame(data)
df.to_csv('ISSCis.csv')


