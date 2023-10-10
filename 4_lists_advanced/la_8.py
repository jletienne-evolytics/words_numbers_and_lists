#a list of numbers
numbers = [10,11,12,13,14,15]
fruits = ['apple', 'grape', 'pear', 'mango']

#let's change drinks
drinks = [['hi-c', 'capri-sun', 'orange juice'], ['water']]

full_list = [numbers, fruits, drinks]

final = full_list[2][0][2]

print(final)

#string to list
print(list(final))

#print('list inception #1')
#print(list(final)[5])

#print('list inception #2')
#print(list(final)[:5])
#print(list(final)[:5+1])


#print('list inception #3')
#print(list(final)[5:9])

#print('list inception #4')
#print(final[5:9])
#print(final[5])

#print('list inception #5')
#print(final[:5])
#print(final[:5+1])


#print('list inception #6')
#print(final[6:])
