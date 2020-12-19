import requests
import json
from datetime import datetime
from datetime import date, timedelta
import base64
import pandas as pd
import time

consumer_key = '31fWqbjyxpLFSCfducjlE023w'
consumer_secret = '5TV3AvBsbYLVYL9LoFf7WK6CUskHTyV68QRdO5Cr9tApwVIFK6'
access_token = '911694428925960193-oxyVrPtNV3GAFc8xJVmQn6V1gK14bVX'
access_secret = 'YBwQ214yVGyenDTvc1U4kwKajUgZ3LQa6ezaafXFh5ILc'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAF1tJQEAAAAAKYcSAgdWgeh%2BCsya5iwuhiqqlvc%3DOB3dX8yqZnWHLlskuYUZYLztWvDfhQMd3UFMs043jEOBO6ZD0f'

key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

# auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# print(auth_resp.text)
# print(auth_resp.status_code)

# access_token = auth_resp.json()['access_token']
# with open('data/bearer_token.json', 'w') as output_file:
#     json.dump(access_token, output_file)


sdate = date(2020,4,18)   
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

# day = '2020-03-12 0000'
# date = str(day).replace('-','').split(' ')[0]
# params = {
#     'query' : 'tesla lang:en',
#     'maxResults' : '100',
#     'fromDate' : date + '0000',
#     'toDate' : date + '2359'
# }

# header = {
#     'Authorization' : 'Bearer {}'.format(bearer_token)
# }

# response = requests.post("https://api.twitter.com/1.1/tweets/search/fullarchive/finalProject.json", json=params, headers=header)
# data = response.json()



# output_file_name = 'results_' + params['fromDate']#str(datetime.now()).replace(' ', '_').replace(':', '').split('.')[0]

# with open('data/' + output_file_name + '.json', 'w') as output_file:
#     json.dump(data, output_file)