# in this program if the user input name matches the list of presaved names, access is granted to open private files and folders
# names are provided in list_of_names.txt file.

def permission_decorator(func):
    def wrapper(*args, **kwargs):
        
        print(f'Calling {func.__name__}() function to check identity...')
        import time
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper

@permission_decorator
def permissions(n):

    with open('D:/PROGRAMMING/Python/projects/list_of_names.txt', 'r') as names:
        content = list(names.read().split(' '))
        if n in content:
            # if True:
            return True
            
        return False
     
name = input('Enter your First Name: ')
if permissions(name):
    print(f'\n{name}: ACCESS GRANTED')

    import os
    print(f'Hello {name}, Welcome!')
    print('\nHere is a list of directories. WOULD YOU LIKE TO OPEN ANY FILES?\n%s.' % ', '.join(os.listdir('D:/PROGRAMMING/Python')))
    
    choice1 = input('\nYes or No: ')

    if choice1 == 'Yes':
        choice2 = input('Enter the path to the file: ') # D:\PROGRAMMING\Python\birthdays\leah.txt
        file1 = open(choice2, 'r')
        print('\n'.join(file1.readlines()))

else:
    print(f'\n{name}: ACCESS NOT GRANTED.')
