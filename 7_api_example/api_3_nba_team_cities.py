#if you get an installation error
#$ pip install requests
import requests

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

print(team_city_list)
