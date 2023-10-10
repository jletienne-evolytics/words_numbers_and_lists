

#Loops are core to automation they allow to execute similar code
#I put loops last because it's best to start at the base case

nums = 50
for i in range(nums):
    if i % 2 == 1:
        print(f'{i} is odd')
    else:
        print(f'{i} is even')

#prints numbers 0 to 49
