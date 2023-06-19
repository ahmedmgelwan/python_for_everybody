'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
'''

largest = None
smallest = None

while True:
    num = input('Enter an integer number: ')
    if num == 'done': break
    try:
        num = int(num)
        if largest is None or num > largest: # Must be in this order to be able to check if largest is None or it will be false becouse we can not compare int with None
            largest = num

        if smallest is None or num < smallest:
            smallest = num

    except:
        print('Invalid input')

print('Maximum is', largest)
print('Minimum is', smallest)