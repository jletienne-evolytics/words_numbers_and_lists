

#define a function called main
def main():
    name = 'Tom'
    age = 22
    return f'My name is {name}, I am {age} years old'

#does not execute
def main2():
    name = 'Robert'
    age = 18

    return f'And my name is {name}, I am {age} years old'

#boilerplate
if __name__ == '__main__':
    x = main()
    print(x)
