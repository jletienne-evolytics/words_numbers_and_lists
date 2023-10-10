

#define a function called main, with variable paramenters name and age
def main(name='Tom', age=22):
    return f'My name is {name}, I am {age} years old'

#boilerplate
if __name__ == '__main__':
    name1='Tom'
    age1=22
    x = main(name1, age1)

    name2='Robert'
    age2=18
    y = main(name2, age2)

    print(x)
    print()
    print(y)
    #print(y + '! lets gooooo')
