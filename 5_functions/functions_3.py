#previously everything we've done starts on line 1
#this file "starts" on line 12! with __name__ == '__main__'

#define a function called main
def main():
    name = 'Tom'
    age = 22
    return f'My name is {name}, I am {age} years old'


#boilerplate
#executes first!
if __name__ == '__main__':
    x = main()
    print(x)
