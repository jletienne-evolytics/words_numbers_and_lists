
#####setup
#if you get an error that says
#ModuleNotFoundError: No module named 'requests'
#make sure you have your virtual environment active!
#$ pip install requests
#####
import requests


#The average age of person, passing a name
#More info https://agify.io/#overview

#define function, with Bella as default
def get_age_from_name(name='Bella'):
    url = f'https://api.agify.io/?name={name}'

    x = requests.get(url)

    return x.json()


if __name__ == '__main__':
    name = 'Tyson'
    x = get_age_from_name(name)
    print(x)
