try:
    age=int(input('Enter your age: '))

    if age%2==0:
        print('Your age is even.')
    elif age%2==1:
        print('Your age is odd.')
except ValueError as ex:
    print('Exception: ', ex)
    print('Please try again.')