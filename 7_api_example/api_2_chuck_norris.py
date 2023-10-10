
#####setup
#if you get an error that says
#ModuleNotFoundError: No module named 'requests'
#make sure you have your virtual environment active!
#$ pip install requests
#####
import requests


#Chuck Norris Jokes
def get_random_joke():
    url = f'https://api.chucknorris.io/jokes/random'

    x = requests.get(url)

    #return x.json()
    return x.json()['value']


if __name__ == '__main__':
    x = get_random_joke()
    print(x)
