
#####setup
#if you get an error that says
#ModuleNotFoundError: No module named 'requests'
#make sure you have your virtual environment active!
#$ pip install requests
#####
import requests
import sys


#Chuck Norris Jokes
def get_random_joke():
    url = f'https://api.chucknorris.io/jokes/random'

    x = requests.get(url)

    #return x.json()
    return x.json()['value']


def create_joke_list(number_of_jokes=3):
    jokes = []
    for i in range(number_of_jokes):
        new_joke = get_random_joke()
        jokes.append(get_random_joke())

    return jokes


if __name__ == '__main__':


    #error handling
    try:
        number_of_jokes = int(sys.argv[1])
    except:
        number_of_jokes = 3

    print(f'finding {number_of_jokes} joke(s)!')
    print('')


    jokes = create_joke_list(number_of_jokes)

    for i in range(len(jokes)):
        print(f'joke {i+1}: {jokes[i]}')
        print('')


'''
here type this in the terminal

$ python get_random_joke 3

'''
