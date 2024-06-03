def addition(a, b):
    return a+b
def subtraction(a, b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a, b):
    return a/b

# get user input, accept numerical input
while True:
    a = input('Enter your 1st number: ')
    b = input('Enter your 2nd number: ')
    # convert strings to int or float
    if ('.' in a):
        a = float(a)
    else:
        a = int(a)
    if ('.' in b):
        b = float(b)
    else:
        b = int(b)

    while True:
        direction = input('Would you like to continue (y/n)?: ')
        if direction != 'y':
            break
        
        print('\nChoose one of the following operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n')
        choice = int(input('Enter the number of your choice: '))
        if not 1 <= choice <= 4:
            print('This option does not exist.')
        elif choice == 1:
            print('The addition of', a,'and', b, 'is', addition(a, b))
        elif choice == 2:
            print('The subtraction of', a,'and', b, 'is', subtraction(a, b))
        elif choice == 3:
            print('The multiplication of', a,'and', b, 'is', multiplication(a, b))
        elif choice == 4:
            if b == 0:
                print('The denominator must not be 0.')
                break
            else:
                print('The division of', a,'and', b, 'is', division(a, b))
    break # if your choice was not to continue the out while loop breaks