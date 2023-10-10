
def main(name='Tom', age=22):
    return f'My name is {name}, I am {age} years old'

#boilerplate
if __name__ == '__main__':
    person1={'name': 'Robert', 'age': 18}
    x = main(person1['name'], person1['age'])

    person2={'name': 'Jim', 'age': 17}
    y = main(person2['name'], person2['age'])

    print(x)
    print()
    print(y)
