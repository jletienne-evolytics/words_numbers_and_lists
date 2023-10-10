#if you get an installation error
#$ pip install requests
#$ pip install pandas

import requests
import pandas as pd

#base url
url = f'https://www.balldontlie.io/api/v1/teams'

#use requests method to "get" data
x = requests.get(url)

#response 200, json == dictionary for our purposes.
teams = x.json()

#blank list
team_city_list = []

#for loop for automation
for team in teams['data']:
    #append each to a list
    team_city_list.append(team['city'])


team_df = pd.DataFrame(team_city_list)

#rename columns
team_df.columns = ['nba_team_city']

#write it to a csv
team_df.to_csv('prod_data/nba_team_city_list.csv', index=False, header=True)
