

#define a function called main
def main():
    name = 'Tom'
    age = 22
    return f'My name is {name}, I am {age} years old'

#does not execute
def main2():
    name = 'Robert'
    age = 18

    return f'And I\'m {name}, I\'m {age}'

#boilerplate
if __name__ == '__main__':
    x = main()
    #x = main
    y = main2()


    print(x)
    #print(x + ' ' + y)

    #presented as an f-string
    #print(f'{x}. {y}!')
