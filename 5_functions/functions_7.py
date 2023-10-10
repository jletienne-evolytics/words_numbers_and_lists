

#define a function called main, with variable paramenters name and age
def main(name='Tom', age=22):
    return f'My name is {name}, I am {age} years old'

#boilerplate
if __name__ == '__main__':
    name1='Tom'
    age1=22
    x = main(name1,age1)
    print(x)
