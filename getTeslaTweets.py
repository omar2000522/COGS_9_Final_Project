import requests
import json
from datetime import datetime
from datetime import date, timedelta
import pandas as pd
import time


bearer_token = 'YOUR_BEARER_TOKEN'


sdate = date(2020,1,1)   
edate = date(2020,6,20)  

for day in pd.date_range(sdate,edate-timedelta(days=1),freq='d').tolist():
    time.sleep(3)
    date = str(day).replace('-','').split(' ')[0]
    params = {
        'query' : 'tesla lang:en',
        'maxResults' : '100',
        'fromDate' : date + '0000',
        'toDate' : date + '2359'
    }

    header = {
        'Authorization' : 'Bearer {}'.format(bearer_token)
    }

    response = requests.post("https://api.twitter.com/1.1/tweets/search/fullarchive/gathering.json", json=params, headers=header)
    data = response.json()



    output_file_name = 'results_' + params['fromDate']#str(datetime.now()).replace(' ', '_').replace(':', '').split('.')[0]

    with open('data/' + output_file_name + '.json', 'w') as output_file:
        json.dump(data, output_file)
