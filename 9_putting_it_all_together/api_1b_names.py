#####setup
#if you get an error that says
#ModuleNotFoundError: No module named 'requests'
#make sure you have your virtual environment active!
#$ pip install requests
#$ pip install pandas
#####
import requests
import pandas as pd

def get_names():
    names = pd.read_csv('raw_data/names.csv')
    return names

#define function, with Bella as default
def get_age_from_name(name='Bella'):
    url = f'https://api.agify.io/?name={name}'

    x = requests.get(url)

    return x.json()

#read_csv file
name_list = get_names()['names'][0:4]

#create blank list
all_names = []

#for loop, loop through the data
for name in name_list:
    x = get_age_from_name(name)
    all_names.append(x)


final_df = pd.DataFrame(all_names)
final_df.to_csv('prod_data/final_names.csv', header=True, index=False)
