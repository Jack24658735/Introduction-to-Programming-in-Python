try:
    A = input('Enter A: ')
    B = input('Enter B: ')
    numA = int(A)
    numB = int(B)    
    quotient = numA / numB
    print('There is no exception.')
    print(f'quotient = {quotient:6f}')
except ZeroDivisionError:
    quotient = -1.0
    print('There is an exception. It is ZeroDivisionError.')
    print(f'quotient = {quotient:6f}')
except ValueError:
    quotient = -1.0
    print('There is an exception. It is ValueError.')
    print(f'quotient = {quotient:6f}')


    
