## Conditional statements

num=3
if num > 0:
    print(num,' is positive')

num=-1
if num > 0 :
    print(num,' is positive')

## Program checks if the numbers is positive or negative
# and displays an appropreate message

num=5
if num >= 0 :
    print(num,' is positive')

else:
    print(num,' is negative')

## check if number is positive, negative or zero

#num=2
#num=0
num=-3

if num > 0:
    print(num,' is positive')
elif num==0:
    print(num,' is zero')
else:
    print(num,' is negative')

# The symbol "%" in python is calledthe 'Modulo'. It returns the remainder
#2%2=0
#3%2=1

## Nested if else

n=5

if n >= 0:
    if n==0:
        print('number is zero')
    else:
        print('number is positive')
else:
    print('number is negative')
    
    
